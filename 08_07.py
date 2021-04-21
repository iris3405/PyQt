import pyupbit 

access_key = "rudr1srMrxFdcMtV578ug17GCOwvgOf1iLZQxgpj"
secret_key = "vVmpSDxNnwGn1k2O7PDLIc9qDdP9Fom2j38M6Iew"

 
upbit = pyupbit.Upbit(access_key, secret_key)
ret = upbit.cancel_order('cc52be46-1000-4126-aee7-9bfafb867682')
print(ret)