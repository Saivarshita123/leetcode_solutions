import re
from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        
        allowed_business = ["electronics", "grocery", "pharmacy", "restaurant"]
        business_order = {b: i for i, b in enumerate(allowed_business)}
        
        valid = []
        
        for c, b, active in zip(code, businessLine, isActive):
            # Must be active
            if not active:
                continue
            
            # Valid business line
            if b not in business_order:
                continue
            
            # Code must be non-empty and alphanumeric + underscore
            if not c or not re.fullmatch(r"[A-Za-z0-9_]+", c):
                continue
            
            valid.append((business_order[b], c))
        
        # Sort by business order, then by code
        valid.sort()
        
        return [c for _, c in valid]
