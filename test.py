import os
if os.path.exists("/srv/offers/backend/web/pdf/contract_kips.html"):
    print("File exists!")
else:
    print("File not found!")
