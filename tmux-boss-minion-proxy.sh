#!/bin/bash

CMD_SERVER="python tp_multithreading/src/queue_manager.py"
CMD_PROXY="python tp_multithreading/src/proxy.py"
CMD_BOSS="python tp_multithreading/src/boss.py 100"
CMD_MINION_PY="python tp_multithreading/src/minion.py"
CMD_MINION_CPP="./build/low_level"

tmux new-session -d -s my_session \; \
    split-window -v \; \
    send-keys "$CMD_SERVER" C-m \; \
    split-window -h \; \
    send-keys "$CMD_PROXY" C-m \; \
    split-window -h \; \
    send-keys "$CMD_BOSS" C-m \; \
    select-pane -t 0 \; \
    send-keys "$CMD_MINION_CPP" C-m \; \
    split-window -h \; \
    send-keys "$CMD_MINION_PY" C-m \; \
    select-pane -t 0 \; \
    attach-session -t my_session
