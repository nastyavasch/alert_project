#!/bin/bash
declare freq="60Min"
declare col="bundle_id"

poetry run python main.py start $freq $col