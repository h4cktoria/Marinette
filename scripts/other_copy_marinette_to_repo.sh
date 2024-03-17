#!/usr/bin/env bash

./scripts/install_marinette.py
rm -rf ../Marinette/* && yes | cp -r * ../Marinette/
