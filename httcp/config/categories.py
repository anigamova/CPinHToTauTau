# coding: utf-8

"""
Definition of categories.
"""

import order as od

from columnflow.config_util import add_category


def add_categories(config: od.Config) -> None:
    """
    Adds all categories to a *config*.
    ids from 1 to 9 are reserved for channels
    ids from 10 to 990 are reserved for helper categories like mt cut or same/opposite sign selection
    ids from 1000 to 990000 are reserved for actual signal, application and determination regions
    """
    
    add_category(
        config,
        name="incl",
        id=1,
        selection="cat_incl",
        label="inclusive",
    )
    
    ##############################################
    ### Main categories for the three channels ###
    ##############################################
    mutau = add_category(
        config,
        name="cat_mutau",
        id=2,
        selection="cat_mutau",
        label=r"$\mu\tau$ inclusive",
    )
    
    etau = add_category(
        config,
        name="cat_etau",
        id=3,
        selection="cat_etau",
        label=r"$e\tau$ inclusive",
    )
    
    tautau = add_category(
        config,
        name="cat_tautau",
        id=4,
        selection="cat_tautau",
        label=r"$\tau\tau$ inclusive",
    )
    ##############################################
    ### Main categories for the three channels ###
    ##############################################
    
    #############################################
    ### Categories for the Fake Factor method ###
    #############################################
    
    os_charge = add_category(
        config,
        name="os_charge",
        id=10,
        selection="os_charge",
        label=r"$q_1\cdot q_2 < 0$",
    )
    
    ss_charge = add_category(
        config,
        name="ss_charge",
        id=20,
        selection="ss_charge",
        label=r"$q_1\cdot q_2 > 0$",
    )
    
    mT_cut = add_category(
        config,
        name="mt_cut",
        id=30,
        selection="mt_cut",
        label=r"$mT < 50$ GeV",
    )
    
    mT_inv_cut = add_category(
        config,
        name="mt_inv_cut",
        id=40,
        selection="mt_inv_cut",
        label=r"$mT \geq 50$ GeV",
    )
    
    deep_tau_wp = add_category(
        config,
        name="deep_tau_wp",
        id=50,
        selection="deep_tau_wp",
        label="DeepTau wp",
    )
    deep_tau_inv_wp = add_category(
        config,
        name="deep_tau_inv_wp",
        id=60,
        selection="deep_tau_inv_wp",
        label="inv DeepTau",
    )
    b_veto = add_category(
        config,
        name="b_veto",
        id=70,
        selection="b_veto",
        label="b veto",
    )
    b_veto_inv = add_category(
        config,
        name="b_veto_inv",
        id=80,
        selection="b_veto_inv",
        label="inv b veto",
    )

    mutau_dm0 = add_category(
        config,
        name="decay_mode_lpi",
        id=90,
        selection="decay_mode_lpi",
        label="tau PNet DM = 0",
    )
    mutau_dm1 = add_category(
        config,
        name="decay_mode_lrho",
        id=100,
        selection="decay_mode_lrho",
        label="tau PNet DM = 1",
    )

    mutau_dm2 = add_category(
        config,
        name="decay_mode_la1",
        id=110,
        selection="decay_mode_la1",
        label="tau PNet DM = 2",
    )

    #############################################
    ### Categories for the Fake Factor method ###
    #############################################
    
    #################################
    ### mu-tau channel categories ###
    #################################
    
    mutau_signal_reg = add_category(
        config,
        name="mutau_signal_reg",
        id=2000 + mutau.id,
        selection=[mutau.selection,
                   os_charge.selection,
                   mT_cut.selection,
                   deep_tau_wp.selection,
                   b_veto.selection],
        label=r"$\mu\tau$ signal region",
    )

    mutau_signal_reg_mupi = add_category(
        config,
        name="mutau_signal_reg",
        id=2000 + mutau.id,
        selection=[mutau.selection,
                   os_charge.selection,
                   mT_cut.selection,
                   deep_tau_wp.selection,
                   b_veto.selection,
                   mutau_dm0.selection],
        label=r"$\mu\tau$ signal region tau DM0",
    )

    mutau_signal_reg_murho = add_category(
        config,
        name="mutau_signal_reg",
        id=2000 + mutau.id,
        selection=[mutau.selection,
                   os_charge.selection,
                   mT_cut.selection,
                   deep_tau_wp.selection,
                   b_veto.selection,
                   mutau_dm1.selection],
        label=r"$\mu\tau$ signal region tau DM1",
    )

    mutau_signal_reg_mua1 = add_category(
        config,
        name="mutau_signal_reg",
        id=2000 + mutau.id,
        selection=[mutau.selection,
                   os_charge.selection,
                   mT_cut.selection,
                   deep_tau_wp.selection,
                   b_veto.selection,
                   mutau_dm2.selection],
        label=r"$\mu\tau$ signal region tau DM2",
    )

    
    mutau_inv_mt = add_category(
        config,
        name="mutau_inv_deeptau",
        id=1000 + mutau.id,
        selection=[mutau.selection,
                   os_charge.selection,
                   mT_cut.selection,
                   b_veto.selection,
                   deep_tau_inv_wp.selection],
        label=r"$\mu\tau$ inv DeepTau",
    )
    mutau_inv_mt = add_category(
        config,
        name="mutau_inv_mt",
        id=3000 + mutau.id,
        selection=[mutau.selection,
                   os_charge.selection,
                   mT_inv_cut.selection,
                   b_veto.selection,
                   deep_tau_wp.selection],
        label=r"$\mu\tau$ inv mt",
    )
    mutau_no_mt = add_category(
        config,
        name="mutau_no_mt",
        id=4000 + mutau.id,
        selection=[mutau.selection,
                   os_charge.selection,
                   b_veto.selection,
                   deep_tau_wp.selection],
        label=r"$\mu\tau$ no mt",
    )
    
    mutau_ff_control_reg = add_category(
        config,
        name="mutau_ff_control_reg",
        id=5000 + mutau.id,
        selection=[mutau.selection,
                   ss_charge.selection,
                   mT_cut.selection,
                   deep_tau_wp.selection,
                   b_veto.selection],
        label=r"$\mu\tau$ control region",
    )
    
    #################################
    ### mu-tau channel categories ###
    #################################
    
    ################################
    ### e-tau channel categories ###
    ################################
    
    etau_signal_reg = add_category(
        config,
        name="etau_signal_reg",
        id=3000 + etau.id,
        selection=[etau.selection,
                   os_charge.selection,
                   mT_cut.selection,
                   deep_tau_wp.selection,
                   b_veto.selection],
        label=r"$e\tau$ signal region",
    )
    etau_ff_control_reg = add_category(
        config,
        name="etau_ff_control_reg",
        id=5000 + etau.id,
        selection=[etau.selection,
                   ss_charge.selection,
                   mT_cut.selection,
                   deep_tau_wp.selection,
                   b_veto.selection],
        label=r"$e\tau$ control region",
    )
    etau_inv_deeptau = add_category(
        config,
        name="etau_inv_deeptau",
        id=4000 + etau.id,
        selection=[etau.selection,
                   os_charge.selection,
                   mT_cut.selection,
                   b_veto.selection,
                   deep_tau_inv_wp.selection],
        label=r"$e\tau$ inv DeepTau",
    )
    
    etau_no_mt = add_category(
        config,
        name="etau_no_mt",
        id=2000 + etau.id,
        selection=[etau.selection,
                   os_charge.selection,
                   b_veto.selection,
                   deep_tau_wp.selection],
        label=r"$e\tau$ no mt",
    )
    
    ################################
    ### e-tau channel categories ###
    ################################
