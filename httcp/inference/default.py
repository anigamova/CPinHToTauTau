# coding: utf-8

from columnflow.inference import inference_model, ParameterType, ParameterTransformation

process_names = [
    "dy_z2ee",
    "dy_z2mumu",
    "dy_z2tautau",
    "wj",
    "vv", #diboson inclusive
    "tt",
    "st",
]
categories = ["mutau_signal_reg", "mutau_inv_deeptau", "mutau_inv_mt", "mutau_no_mt", "mutau_ff_control_reg"]

@inference_model
def default_htt(self):

    #
    # categories
    #

    self.add_category(
        "mutau_SR_mupi",
        config_category="mutau_signal_reg_mupi",
        config_variable="phi_cp",
        mc_stats=True,
    )

    self.add_category(
        "mutau_SR_murho",
        config_category="mutau_signal_reg_murho",
        config_variable="phi_cp",
        mc_stats=True,
    )

    self.add_category(
        "mutau_SR_mua1",
        config_category="mutau_signal_reg_mua1",
        config_variable="phi_cp",
        mc_stats=True,
    )

    self.add_category(
        "mutau_ff_control_reg",
        config_category="mutau_ff_control_reg",
        config_variable="mutau_mvis",
        mc_stats=True,
    )

    #
    # processes
    #

    for process in process_names: 

        self.add_process(
            process,
            is_signal=("h_" in process),
            config_process=process,
        )
    
    #
    # parameters
    #

    # groups
    self.add_parameter_group("experiment")
    self.add_parameter_group("theory")

    # lumi
    lumi = self.config_inst.x.luminosity
    for unc_name in lumi.uncertainties:
        self.add_parameter(
            unc_name,
            type=ParameterType.rate_gauss,
            effect=lumi.get(names=unc_name, direction=("down", "up"), factor=True),
            transformations=[ParameterTransformation.symmetrize],
        )

