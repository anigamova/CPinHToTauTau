#!/bin/bash
source ./common.sh #to access set_common_vars() function
#The following function defines config, processes, version and datasets variables
set_common_vars "$1"
args=(
        --config $config
        --processes $processes
        --version $version
        --datasets $datasets
        --workflow local
        --selector-steps trigger,met_filter,b_veto,selected_hcand,selected_hcand_trigmatch,dilepton_veto,extra_lepton_veto,single_hcand,decay_prods_are_ok
        "${@:2}"
    )
echo run cf.PlotCutflow "${args[@]}"
law run cf.PlotCutflow "${args[@]}"