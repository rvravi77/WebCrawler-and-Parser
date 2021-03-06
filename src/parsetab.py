
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALL COLLECTION E_ANKOR E_BIDAY E_BR E_DIV E_LNAME E_MOVIE E_OMT E_RUNTI E_SPAN H_RATE LLINK L_RATE S_BIDAY S_BOXOF S_CHAR S_DIREC S_GENRE S_LANGU S_LNAME S_MOVIE S_NAME S_OMT S_PRODU S_RUNTI S_STAR S_SYNOP S_WRITE S_WTW TROWstart : TROW S_OMT E_OMTstart : S_BIDAY ALL E_BIDAYstart : H_RATE ALL E_ANKORstart : L_RATE ALL E_ANKORstart : S_WTW ALLstart : S_LNAME ALL E_LNAMEstart : LLINK ALLstart : S_GENRE ALL E_DIVstart : S_STAR ALL E_SPAN S_CHAR ALL E_BR\n             | S_STAR ALL E_SPAN S_CHAR ALL E_SPANstart : S_WRITE termw E_DIV\n       termw : termw endw\n             | S_NAME ALL E_ANKOR ALL\n       endw  : S_NAME ALL E_ANKOR ALLstart : S_PRODU termp E_DIV\n       termp : termp endp\n             | S_NAME ALL E_ANKOR ALL\n       endp  : S_NAME ALL E_ANKOR ALLstart : S_MOVIE ALL E_MOVIEstart : S_DIREC ALL E_ANKORstart : S_LANGU ALL E_DIVstart : S_SYNOP ALL E_DIVstart : S_BOXOF COLLECTION E_DIVstart : S_RUNTI ALL E_RUNTI'
    
_lr_action_items = {'TROW':([0,],[2,]),'S_BIDAY':([0,],[3,]),'H_RATE':([0,],[4,]),'L_RATE':([0,],[5,]),'S_WTW':([0,],[6,]),'S_LNAME':([0,],[7,]),'LLINK':([0,],[8,]),'S_GENRE':([0,],[9,]),'S_STAR':([0,],[10,]),'S_WRITE':([0,],[11,]),'S_PRODU':([0,],[12,]),'S_MOVIE':([0,],[13,]),'S_DIREC':([0,],[14,]),'S_LANGU':([0,],[15,]),'S_SYNOP':([0,],[16,]),'S_BOXOF':([0,],[17,]),'S_RUNTI':([0,],[18,]),'$end':([1,23,25,38,39,40,41,42,43,45,49,53,54,55,56,57,58,69,70,],[0,-5,-7,-1,-2,-3,-4,-6,-8,-11,-15,-19,-20,-21,-22,-23,-24,-10,-9,]),'S_OMT':([2,],[19,]),'ALL':([3,4,5,6,7,8,9,10,13,14,15,16,18,29,31,47,51,59,61,63,65,67,],[20,21,22,23,24,25,26,27,32,33,34,35,37,48,52,60,62,64,66,68,71,72,]),'S_NAME':([11,12,28,30,46,50,66,68,71,72,],[29,31,47,51,-12,-16,-13,-17,-14,-18,]),'COLLECTION':([17,],[36,]),'E_OMT':([19,],[38,]),'E_BIDAY':([20,],[39,]),'E_ANKOR':([21,22,33,48,52,60,62,],[40,41,54,61,63,65,67,]),'E_LNAME':([24,],[42,]),'E_DIV':([26,28,30,34,35,36,46,50,66,68,71,72,],[43,45,49,55,56,57,-12,-16,-13,-17,-14,-18,]),'E_SPAN':([27,64,],[44,69,]),'E_MOVIE':([32,],[53,]),'E_RUNTI':([37,],[58,]),'S_CHAR':([44,],[59,]),'E_BR':([64,],[70,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'termw':([11,],[28,]),'termp':([12,],[30,]),'endw':([28,],[46,]),'endp':([30,],[50,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> TROW S_OMT E_OMT','start',3,'p_o_movie','task2.py',175),
  ('start -> S_BIDAY ALL E_BIDAY','start',3,'p_biday','task2.py',181),
  ('start -> H_RATE ALL E_ANKOR','start',3,'p_hrate','task2.py',186),
  ('start -> L_RATE ALL E_ANKOR','start',3,'p_lrate','task2.py',191),
  ('start -> S_WTW ALL','start',2,'p_wtw','task2.py',196),
  ('start -> S_LNAME ALL E_LNAME','start',3,'p_lname','task2.py',202),
  ('start -> LLINK ALL','start',2,'p_llink','task2.py',208),
  ('start -> S_GENRE ALL E_DIV','start',3,'p_genre','task2.py',214),
  ('start -> S_STAR ALL E_SPAN S_CHAR ALL E_BR','start',6,'p_star','task2.py',220),
  ('start -> S_STAR ALL E_SPAN S_CHAR ALL E_SPAN','start',6,'p_star','task2.py',221),
  ('start -> S_WRITE termw E_DIV','start',3,'p_write','task2.py',235),
  ('termw -> termw endw','termw',2,'p_write','task2.py',236),
  ('termw -> S_NAME ALL E_ANKOR ALL','termw',4,'p_write','task2.py',237),
  ('endw -> S_NAME ALL E_ANKOR ALL','endw',4,'p_write','task2.py',238),
  ('start -> S_PRODU termp E_DIV','start',3,'p_produ','task2.py',244),
  ('termp -> termp endp','termp',2,'p_produ','task2.py',245),
  ('termp -> S_NAME ALL E_ANKOR ALL','termp',4,'p_produ','task2.py',246),
  ('endp -> S_NAME ALL E_ANKOR ALL','endp',4,'p_produ','task2.py',247),
  ('start -> S_MOVIE ALL E_MOVIE','start',3,'p_movie','task2.py',253),
  ('start -> S_DIREC ALL E_ANKOR','start',3,'p_direc','task2.py',258),
  ('start -> S_LANGU ALL E_DIV','start',3,'p_langu','task2.py',263),
  ('start -> S_SYNOP ALL E_DIV','start',3,'p_synop','task2.py',269),
  ('start -> S_BOXOF COLLECTION E_DIV','start',3,'p_boxof','task2.py',275),
  ('start -> S_RUNTI ALL E_RUNTI','start',3,'p_runti','task2.py',280),
]
