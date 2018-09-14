select survived, pclass, sibsp, (parch > 0 as fam), fare 
from titanic 
where parch is not null;