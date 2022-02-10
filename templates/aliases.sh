# shellcheck disable=SC2148
alias do_prune_everything='docker system prune -a'

# alias fzcod='code -n $(find ~ -maxdepth 1 -type d 2>/dev/null | fzf)'
# alias fzcof='code -n $(find . -type f 2>/dev/null  | fzf)'
# alias fzged='gedit $(find ~ -maxdepth 1 -type d 2>/dev/null | fzf)'
# alias fzgef='gedit $(find . -type f 2>/dev/null  | fzf)'

alias cdh='cd $(find ~ -maxdepth 1 -type d | fzf)'
# alias cdp='cd $(find ~/Projects ~/PycharmProjects ~/go/src/github.com/my_account -maxdepth 1 -type d | fzf)'
