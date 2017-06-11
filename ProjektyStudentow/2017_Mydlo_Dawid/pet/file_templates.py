# bashrc

new_project_rc_template = '''
project_root=$(pwd)
source {0}
export PET_ACTIVE_PROJECT='{1}'
if [ -f "$project_root/start.local.entry.sh" ]; then
    source "$project_root/start.local.entry.sh"
fi
source {2}
if [ -f "$project_root/start.local.exit.sh" ]; then
    source "$project_root/start.local.exit.sh"
fi
PS1="[{6}] $PS1"
echo -ne "\\033]0;{6} {3}\\007"
if [ -z "$PET_PREV_TAB_NAME" ]; then
    tab_name_at_exit=""
else
    tab_name_at_exit="$PET_PREV_TAB_NAME"
fi
trap '
echo -ne "\\033]0;$tab_name_at_exit\\007"
if [ -f "$project_root/stop.local.entry.sh" ]; then
    source "$project_root/stop.local.entry.sh"
fi
if [ -f "$project_root/stop.local.exit.sh" ]; then
    source "$project_root/stop.local.exit.sh"
fi
source {4}' EXIT
export PET_PREV_TAB_NAME='{1} {3}'
{5}
'''

new_start_sh_template = '''
if [ ! -z "$pet_project_folder" ]; then
    cd "$pet_project_folder"
fi
# add here shell code to be executed while entering project
'''

new_stop_sh_template = '''
# add here shell code to be executed while exiting project
'''


edit_file_popen_template = """
PET_EDITOR=$(grep '^EDITOR==' {0} | sed -n "/EDITOR==/s/EDITOR==//p")
if [ $(command -v "$PET_EDITOR") ]; then
    $PET_EDITOR {1}
else
    if [ $(command -v "$EDITOR") ]; then
        $EDITOR {1}
    else
        echo "haven't found either '$EDITOR', either 'EDITOR==' in pet config - trying vi"
        /usr/bin/vi {1}
    fi
fi
"""

auto_complete_zsh_deploy = """
autoload -U +X compinit && compinit
autoload -U +X bashcompinit && bashcompinit
source "{0}"
"""


task_exec_template = """
if [ -f "{2}" ]; then
    source "{2}"
fi
{0} {1}
if [ -f "{3}" ]; then
    source "{3}"
fi
{4}
"""
