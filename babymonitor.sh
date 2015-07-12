#!/bin/bash

CMD=${1}
DATE=${2}

function show_help {
    echo "This is BabyMonitor."
    echo "Available options: "
    echo "start - To start BabyMonitor"
    echo "stop  - To stop BabyMonitor"
    echo "test  - To run tests"
    echo "graph - To display graph"
    echo "help  - to display this information"
}


function start {
    cd app
    python -u app.py >> ../app.log 2>&1 &
    pid=$!
    PGID=$(ps -o pgid= $pid | grep -o [0-9]*)
    echo $PGID > ../app.pid
    cd ..
}

function stop {
    pid=$(cat app.pid)
    kill -9 -$pid
    rm app.pid
}

function graph {
    cd app
    if [[ -z "$DATE" ]]; then
        python plot_occurences.py
    else
        python plot_occurences.py -d $DATE
    fi
    cd ..
}

function run_tests {
    cd app
    python -m unittest discover -p '*_tests.py'
    cd ..

}

case $CMD in
    'start')
    start
    ;;
    'stop')
    stop
    ;;
    'graph')
    graph $GRAPH $DATE
    ;;
    'test')
    run_tests
    ;;
    'help')
    show_help
    ;;
    *)
    show_help
esac