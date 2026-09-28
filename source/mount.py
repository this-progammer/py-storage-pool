# File : mount.py
# Date : 9/28/2026
# Programmer : Hunter M. *Aether

from api import*

class Mount:
  def __init__(self, name : str, id : int, found : Bool):
    self = self
    name = self.name
    id = self.id
    found = self.found

  def get_mount( self ):
    return self

  def is_found( self )->Bool:
    if self.found != True:
      mov_eax_1("Storage Drive Not Mounted, Because It Was Not Found.\n")
      return False
    mov_eax_1("Storage Drive Was Found, Mounted To API.\n")
    return self.found = True
