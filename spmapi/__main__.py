# -*- coding: utf-8 -*-
import spmapi

print(spmapi.app.router.__dict__)
spmapi.app.run(host="0.0.0.0", port=8000, debug=False)
