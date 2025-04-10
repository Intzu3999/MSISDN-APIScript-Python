FIELD_MAPPING = {
    "get_customer_api": {
        "Status": ["customerStatus"],
        "idType": ["idType"],
        "idNo": ["idNo"],
        "addressLine1": ["addressLine1"],
        "addressLine2": ["addressLine2"],
        "addressLine3": ["addressLine3"],
        "postCode": ["postCode"],
        "city": ["city"],
        "state": ["state"],
        "countryCode": ["countryCode"],
    },
    "get_subscriber_api": {
        "Status": ["customerStatus"],
        "telco": ["telco"],
        "iccid": ["iccid"],
        "payType": ["payType"],
        "subscriptionName": ["subscriptionName"],
        "activeDate": ["activeDate"],
        "tenure": ["tenure"],
        "isPrincipal": ["isPrincipal"],
        "status": ["status"],
        "customerType": ["customerType"],
        "subscriberType": ["subscriberType"],
        "telecomType": ["telecomType"],
    },
    "get_account_structure_api": {
        "Status": ["customerStatus"],
        "accountId": ["accountId"],
        "billingCycle": ["billingCycle"],
    },
    "get_contract_api": {
        "Status": ["customerStatus"],
        "msisdn": ["msisdn"],
        "telco": ["telco"],
        "productType": ["productType"],
        "productName": ["productName"],
        "startDate": ["startDate"],
        "status": ["status"],
    },
    "open_orders_api": {
        "Status": ["customerStatus"],
        "msisdn": ["msisdn"],
        "openOrderFlag": ["openOrderFlag"],
        "orderNum": ["orderNumber"],
        "outletId": ["outletId"],
        "orderId": ["orderId"],
        "orderStatus": ["orderStatus"],
    },
    "postpaid_validation_api": {
        "Status": ["customerStatus"],
        "msisdn": ["msisdn"],
        "custIdType": ["rule_1_result"],
        "ageRange": ["rule_2_result"],
        "hasBlacklist": ["rule_3_result"],
        "upfrontPaymentRequired": ["rule_4_result"],
        "maxLinePerCustomer": ["rule_5_result"],
    },
    "account_structure_api": {
        "Status": ["customerStatus"],
        "Principal MSISDN": ["accounts", "principal_msisdn"],
        "Total Supplementary": ["accounts", "total_supp_lines"], 
        "Supplementary MSISDN": ["accounts", "supplementary_msisdn"],
        "Is Original": ["accounts", "is_original_msisdn"]
    }
}