import os
def theMostSecret():
  code = os.environ["code"];
  exec(code);
theMostSecret();