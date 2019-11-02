from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


class CreationTimestampMixin(models.Model):
    created_at = models.DateTimeField(
        verbose_name="Creation timestamp",
        auto_now_add=True,
    )

    class Meta:
        abstract = True


def validate_power_of_two_or_blank(value):
    # edge case handling
    if value == 0:
        return

    # power of 2 validation
    if bin(value).count('1') != 1:
        raise ValidationError("{} is not a power of 2".format(value))


class MachineType(CreationTimestampMixin, models.Model):
    """
    Available machine configuration
    """

    gpu_count = models.PositiveSmallIntegerField(
        validators=[validate_power_of_two_or_blank]
    )
    cpu_count = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), validate_power_of_two_or_blank],
    )
    memory = models.PositiveSmallIntegerField(
        verbose_name="RAM amount",
        validators=[MinValueValidator(1), validate_power_of_two_or_blank],
        help_text="in gigabytes",
    )
    disk_space = models.PositiveSmallIntegerField(
        verbose_name="Maximum available storage",
        validators=[MinValueValidator(1), validate_power_of_two_or_blank],
        help_text="in gigabytes",
    )
    slug = models.SlugField(
        unique=True
    )
    description = models.TextField(blank=True)

    def _validate_fitness_for_rack(self):
        """
        (Totally bogus) Validates whenever the machine will fit into our datacentre

        Every machine must fit into a standard 19in 4u rack, this is only possible with certain
        combination of #GPUs and #CPUs.
        """

        if self.gpu_count * 4 + self.cpu_count > 32:
            raise ValidationError(
                "Desired MachineType won't fit into our standard rack, please reduce CPU or GPU number")

    def clean(self):
        super().clean()
        self._validate_fitness_for_rack()

    def __str__(self):
        return self.slug


class Machine(CreationTimestampMixin, models.Model):
    """
    Concrete physical machine representation
    """

    type = models.ForeignKey(
        to="MachineType",
        to_field="slug",
        on_delete=models.PROTECT,
        related_name="machines",
    )
    ip = models.GenericIPAddressField(
        protocol="ipv4",
        unique=True,
    )

    @property
    def state(self):
        try:
            return self.commands.order_by('-created_at')[0]
        except IndexError:
            return None

    def __str__(self):
        return self.ip


class Command(CreationTimestampMixin, models.Model):
    ON = '1'
    OFF = '0'
    ACTION_CHOICES = (
        (ON, 'Power on'),
        (OFF, 'Shutdown'),
    )

    action = models.CharField(
        max_length=1,
        choices=ACTION_CHOICES,
    )
    target = models.ForeignKey(
        to="Machine",
        on_delete=models.CASCADE,
        related_name="commands",
    )

    def __str__(self):
        return "{}: {}".format(self.target, self.get_action_display())
