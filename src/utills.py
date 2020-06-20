"""
Utility module
"""

import logging

log = logging.getLogger(__name__)

promo_func_map = {'BOGO': '_check_bogo_cd', 'APPL':'_check_appl_cd', 'CHMK': '_check_cmnk_cd', 'APOM': '_check_apom_cd'}


def apply_code(quant_cd_map):
    """

    :return:
    """
    log.debug("Applying promo code to shopping cart")
    apply_cd_lst = {}
    final_price = 0
    disc_price = 0
    final_dict = {}
    for k, v in promo_func_map.items():
        func = eval(v)
        val = func(quant_cd_map, k, apply_cd_lst)
        disc_price = disc_price + val
    final_dict = _filter_code(apply_cd_lst)

    return disc_price, final_dict


def _filter_code(apply_cd_lst):
    """

    :return:
    """
    #final_dict = apply_cd_lst
    final_dict = {k: v for k, v in apply_cd_lst.items() if v}
    # for k,v in apply_cd_lst.items():
    #     if not v:
    #         del final_dict[k]

    return final_dict


def _check_bogo_cd(quant_cd_map, cd, apply_cd_lst):
    """
    it will apply Buy-One-Get-One-Free Special on Coffee. (Unlimited)
    on cart and return price which has to deducted from final price

    :param quant_cd_map: Dict of products attribute like price , quantity and product code
    :param cd: Product code
    :return: discount price
    """
    log.debug("Applying promo code {}to shopping cart".format(cd))
    price = 0
    apply_cd_lst['BOGO'] = 0
    if 'CF1' in quant_cd_map:
        cf_attr = quant_cd_map['CF1']
        cf_price = float(cf_attr[1])
        if cf_attr[2]:
            cf_qunt = float(cf_attr[2])
        else:
            cf_qunt = 0

        if cf_qunt > 1:
            cf_qunt = cf_qunt // 2
            price = cf_qunt * cf_price
        apply_cd_lst['BOGO'] = -price
        return -price

    else:
        log.debug("Coffe packets are not added to shopping cart")
    return price


def _check_appl_cd(quant_cd_map, cd, apply_cd_lst):
    """
    it will apply If you buy 3 or more bags of Apples, the price drops to $4.50
    on cart and return price which has to deducted from final price

    :param quant_cd_map: Dict of products attribute like price , quantity and product code
    :param cd: Product code
    :return: discount price
    """
    log.debug("Applying promo code {}to shopping cart".format(cd))
    price = 0
    apply_cd_lst['APPL'] = price
    if 'AP1' in quant_cd_map:
        ap_attr = quant_cd_map['AP1']
        ap_price = float(ap_attr[1])
        if ap_attr[2]:
            ap_qunt = float(ap_attr[2])
            if ap_qunt > 2:
                price = -4.5
                apply_cd_lst['APPL'] = price

    return price


def _check_cmnk_cd(quant_cd_map, cd, apply_cd_lst):
    """
    it will apply Purchase a box of Chai and get milk free. (Limit 1)
    on cart and return price which has to deducted from final price

    :param quant_cd_map: Dict of products attribute like price , quantity and product code
    :param cd: Product code
    :return: discount price
    """
    log.debug("Applying promo code {}to shopping cart".format(cd))
    mk_price = 0
    apply_cd_lst['CHMK'] = 0
    if ('CH1' in quant_cd_map) and ('MK1' in quant_cd_map):
        ch_attr = quant_cd_map['CH1']
        ch_price = float(ch_attr[1])
        ch_qunt = ch_attr[2]
        if ch_qunt:
            ch_qunt = float(ch_attr[2])
        if ch_qunt:
            mk_attr = quant_cd_map['MK1']
            mk_qunt = mk_attr[2]
            if mk_qunt:
                mk_qunt = float(mk_attr[2])
            if mk_qunt:
                mk_price = -float(mk_attr[1])

    apply_cd_lst['CHMK'] = mk_price
    return mk_price


def _check_apom_cd(quant_cd_map, cd, apply_cd_lst):
    """
    it will apply Purchase a bag of Oatmeal and get 50% off a bag of Apples
    on cart and return price which has to deducted from final price

    :param quant_cd_map: Dict of products attribute like price , quantity and product code
    :param cd: Product code
    :return: discount price
    """
    log.debug("Applying promo code {}to shopping cart".format(cd))
    price = 0
    apply_cd_lst['APOM'] = price
    if ('OM1' in quant_cd_map) and ('AP1' in quant_cd_map):
        om_attr = quant_cd_map['OM1']
        om_qty = om_attr[2]
        if om_qty:
            ap_attr = quant_cd_map['AP1']
            ap_qty = ap_attr[2]
            ap_price = ap_attr[1]
            if ap_qty:
                price = float(ap_qty) * float(ap_price)
                price = -(price // 2)

    apply_cd_lst['APOM'] = price
    return price


def calculate_price(quant_cd_map):
    """

    :param quant_cd_map: Dict of products attribute like price , quantity and product code
    :return: total price without dicscount
    """
    total_price = 0
    total_item_dict = {}
    for k, v in quant_cd_map.items():
        v_attr = v
        if v_attr[2]:
            val = (float(v_attr[2]) * float(v_attr[1]))
            total_price = total_price + val
            total_item_dict[k] = val

    return total_price, total_item_dict
