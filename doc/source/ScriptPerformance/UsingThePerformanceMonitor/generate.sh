#! /bin/bash

set -e

gaffer screengrab scripts/performanceMonitor.gfr -image images/performanceMonitor.png -editor NodeEditor -selection StandardOptions -nodeEditor.reveal StandardOptions.options.performanceMonitor