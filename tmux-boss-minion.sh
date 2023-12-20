#!/bin/bash

COMMAND_1="python src/boss.py 3000"
COMMAND_2="python src/minion.py"
COMMAND_3="python src/minion.py"
COMMAND_4="python src/queue_manager.py"

tmux new-session -d -s my_session \; \
    split-window -v \; \
    send-keys "$COMMAND_4" C-m \; \
    select-pane -t 0 \; \
    send-keys "$COMMAND_1" C-m \; \
    split-window -h \; \
    send-keys "$COMMAND_2" C-m \; \
    split-window -h \; \
    send-keys "$COMMAND_3" C-m \; \
    select-pane -t 0 \; \
    attach-session -t my_session
