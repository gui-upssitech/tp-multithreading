#!/bin/bash

CMD_SERVER="python tp_multithreading/src/queue_manager.py"
CMD_BOSS="python tp_multithreading/src/boss.py 3000"
CMD_MINION_1="python tp_multithreading/src/minion.py"
CMD_MINION_2="python tp_multithreading/src/minion.py"

tmux new-session -d -s my_session \; \
    split-window -v \; \
    send-keys "$CMD_SERVER" C-m \; \
    split-window -h \; \
    send-keys "$CMD_BOSS" C-m \; \
    select-pane -t 0 \; \
    send-keys "$CMD_MINION_1" C-m \; \
    split-window -h \; \
    send-keys "$CMD_MINION_2" C-m \; \
    select-pane -t 0 \; \
    attach-session -t my_session
