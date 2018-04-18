# -*- encoding:utf-8 -*-
from pypinyin import lazy_pinyin
import pypinyin
import datetime
from sys import argv


class Password(object):

    join_symbols = ["!", "@"]

    def __init__(self, run_level, have_birthday,have_telnum,have_qq,have_idnum,have_lover,have_special,txt_dir):
        self.txt_dir = txt_dir
        self.run_level = run_level
        self.have_birthday = have_birthday
        self.have_telnum = have_telnum
        self.have_qq = have_qq
        self.have_idnum = have_idnum
        self.have_lover = have_lover
        self.have_special = have_special
        

    def convert_to_pinyin(self, chinese_name, style = 0):
        if style == 0:
            s = pypinyin.NORMAL
        elif style == 1:
            s = pypinyin.FIRST_LETTER
        elif style == 2:
            s = pypinyin.INITIALS
        return lazy_pinyin(chinese_name, s)

    def generate_name(self, name):
        pwds = []

        name_normal = lazy_pinyin(name, pypinyin.NORMAL) # [ye, shi, wen]
        name_first = lazy_pinyin(name, pypinyin.FIRST_LETTER) # [y, s, w]
        name_initial = lazy_pinyin(name, pypinyin.INITIALS) # [y, sh, w]

        name_count = len(name)
        if name_count == 2:
            # yeshi
            if self.run_level >= 1:
                pwds.append(name_normal[0]+name_normal[1]) # yeshi
                pwds.append(name_first[0]+name_first[1]) # ys
            if self.run_level >= 2:
                pwds.append(name_normal[1]+name_normal[0]) # shiye
                pwds.append(name_first[1]+name_first[0]) # sy
        elif name_count == 3:
            # yeshiwen
            if self.run_level >= 1:
                pwds.append(name_normal[0]+name_normal[1]+name_normal[2]) # yeshiwen
                pwds.append(name_first[0]+name_first[1]+name_first[2]) # ysw
            if self.run_level >= 2:
                pwds.append(name_normal[1]+name_normal[2]+name_normal[0]) # shiwenye
                pwds.append(name_first[1]+name_first[2]+name_first[0]) # swy
            if self.run_level >= 3:
                pass
        elif name_count ==4:
            pass
        else:
            pass

        return pwds

    def generate_birth(self, birthday):
        pwds = []

        if "/" in birthday:
            birthday = birthday.replace("/", "")
        elif "-" in birthday:
            birthday = birthday.replace("-", "")
        else:
            pass

        # 2016-01-02
        c = datetime.datetime.strptime(birthday, "%Y%m%d")
        if self.run_level >= 1:
            pwds.append(c.strftime("%y%m%d")) # 160102
            pwds.append(c.strftime("%m%d"))   # 0102
            pwds.append(c.strftime("%Y%m%d"))   # 20160102
        if self.run_level >= 2:
            pwds.append(str(c.month) + str(c.day))   # 12
            pwds.append(c.strftime("%y") + str(c.month) + str(c.day)) # 1612
            pwds.append(c.strftime("%Y") + str(c.month) + str(c.day)) # 201612
        if self.run_level >= 3:
            pwds.append(c.strftime("%m%d%y"))
            pwds.append(c.strftime("%d%m%y"))
            pwds.append(c.strftime("%d%m%Y"))
            pwds.append(str(c.day) + str(c.month) + c.strftime("%y"))
            pwds.append(str(c.day) + str(c.month) + c.strftime("%Y"))

        return pwds
    
    def generate_telnum(self,telnum):
        pwds = []
        
        n = telnum
        if self.run_level >= 1:
            pwds.append(n)
            pwds.append(n[7::])
        return pwds
    
    def generate_qq(self,qq):
        pwds = []
        
        i = qq
        if self.run_level >= 1:
            pwds.append(i)
        
        
        return pwds
    
    def generate_idnum(self,idnum):
        pwds = []
        
        i = idnum
        
        if self.run_level >= 1:
            pwds.append(i)
        
        
        return pwds

    def lover_name(self, lover):
        pwds = []

        lover_normal = lazy_pinyin(lover, pypinyin.NORMAL) # [ye, shi, wen]
        lover_first = lazy_pinyin(lover, pypinyin.FIRST_LETTER) # [y, s, w]

        lover_count = len(lover)
        if lover_count == 2:
            # yeshi
            if self.run_level >= 1:
                pwds.append(lover_first[0]+lover_first[1]) # ys
        elif lover_count == 3:
            # yeshiwen
            if self.run_level >= 1:
                pwds.append(lover_first[0]+lover_first[1]+lover_first[2]) # ysw
        elif lover_count ==4:
            pass
        else:
            pass

        return pwds

    def special_num(self,special):
        pwds = []

        s = special

        if self.run_level >= 1:
            pwds.append(s)

        return pwds



        
    
        
    
    def mix_name_birth(self, name_pwds, birth_pwds):
        pwds = []
        for name in name_pwds:
            for birth in birth_pwds:
                if self.run_level >= 1:
                    pwds.append(name+birth)
                    
                if self.run_level >= 2:
                    pwds.append(birth+name)
                if self.run_level >= 3:
                    for sym in self.join_symbols:
                        pwds.append(name+sym+birth)
                        pwds.append(birth+sym+name)
        return pwds
    
    def mix_name_telnum(self,name_pwds,telnum_pwds):
        pwds = []
        
        for telnum in telnum_pwds:
            if self.run_level >= 1:
                if len(telnum) == 0:
                    break
                else:
                    pwds.append(telnum)
            if self.run_level >= 2:
                if len(telnum) == 0:
                    break
                else:
                    
                    for name in name_pwds:
                        pwds.append(name+telnum)
                        pwds.append(telnum+name)
            if self.run_level >= 3:
                if len(telnum) == 0:
                    break
                else:
                    for name in name_pwds:
                        for sym in self.join_symbols:
                            pwds.append(name+sym+telnum)
                            pwds.append(telnum+sym+name)
        return pwds
    
    def mix_name_qq(self,name_pwds,qq_pwds):
        pwds = []
        for qq in qq_pwds:
            if self.run_level >= 1:
                if len(qq) == 0:
                    break
                else:
                    pwds.append(qq)
            if self.run_level >= 2:
                if len(qq) == 0:
                    break
                else:
                    for name in name_pwds:
                        pwds.append(name+qq)
                        pwds.append(qq+name)
            if self.run_level >= 3:
                if len(qq)==0:
                    break
                else:
                    for name in name_pwds:
                        for sym in self.join_symbols:
                            pwds.append(name+sym+qq)
                            pwds.append(qq+sym+name)
        return pwds
    
    def mix_name_idnum(self,name_pwds,id_pwds):
        pwds = []
        for idnum in id_pwds:
            if self.run_level >= 1:
                if len(idnum) == 0:
                    break
                else:
                    pwds.append(idnum)
            if self.run_level >= 2:
                if len(idnum) == 0:
                    break
                else:
                    for name in name_pwds:
                        pwds.append(name+idnum)
                        pwds.append(idnum+name)
            if self.run_level >= 3:
                if len(idnum) == 0:
                    break
                else:
                    for name in name_pwds:
                        for sym in self.join_symbols:
                            pwds.append(name+sym+idnum)
                            pwds.append(idnum+sym+name)
        return pwds
    
    def mix_name_lover(self,name_pwds,lover_pwds):
        pwds = []
        for lover in lover_pwds:
            if self.run_level >= 1:
                if len(lover) == 0:
                    break
                else:
                    pwds.append(lover +"520")
                    pwds.append(lover + "5201314")
                    pwds.append("5201314"+lover)
                    pwds.append("520"+lover)
            if self.run_level >= 2:
                if len(lover) == 0:
                    break
                else:
                    for name in name_pwds:
                        pwds.append(name+lover)
                        pwds.append(lover+name)
            if self.run_level >= 3:
                if len(lover) == 0:
                    break
                else:
                    for sym in self.join_symbols:
                        pwds.append(name+sym+lover)
                        pwds.append(lover+sym+name)
        return pwds
    def mix_special(self,name_pwds,lover_pwds,special_pwds):
        pwds = []
        for special in special_pwds:
            if self.run_level >= 1:
                if len(special) == 0:
                    break
                else:
                    for name in name_pwds:
                        
                        pwds.append(special)
                        pwds.append(name+special)
                        pwds.append(special + name)
            if self.run_level >= 2:
                if len(special) == 0:
                    break
                else:
                    for name in name_pwds:
                        for lover in lover_pwds:
                            
                            pwds.append(name+lover+special)
                            pwds.append(name+special+lover)
                            pwds.append(lover+special+name)
            if self.run_level >= 3:
                if len(special) == 0:
                    break
                else:
                    for lover in lover_pwds:
                        pwds.append(lover+special)
                        pwds.append(special+lover)
                        
        return pwds

    
           
    def process_txt(self):
        infos = []
        file = open(self.txt_dir, "r",encoding='UTF-8')
        for line in file.readlines():
            line = line.replace("\r","").replace("\n","")
            tmp = []
            if self.have_birthday:
                x = line.split("\t")
                tmp.append(x[0])
                tmp.append(x[1])
            if self.have_telnum:
                x = line.split("\t")
                tmp.append(x[2])
            if self.have_qq:
                x = line.split("\t")
                tmp.append(x[3])
            if self.have_idnum:
                x = line.split("\t")
                tmp.append(x[4])
            if self.have_lover:
                x = line.split("\t")
                tmp.append(x[5])
            if self.have_special:
                x = line.split("\t")
                tmp.append(x[6])
            
            else:
                tmp.append(line)
            infos.append(tmp)
        return infos

    def weak_password(self):
        '''
        weak password example
        '''
        weak_pwds = []
        if self.run_level >= 1:
            pwds = ["123456wsa", "qwe123","8888888"]
            weak_pwds.extend(pwds)
        if self.run_level >= 2:
            pwds = ["123456789", "1234qwer", "1qaz2wsx"]
            weak_pwds.extend(pwds)
        if self.run_level >= 3:
            pwds = ["123!@#", "!qaz@wsx","88888888","123456789"]
            weak_pwds.extend(pwds)
        return weak_pwds

    def weak_suffix(self, pwds):
        if self.run_level >= 1:
            pass
        if self.run_level >= 2:
            pass
        if self.run_level >= 3:
            pass

    def run(self):

        pwds = []
        # name = u"鍙惰瘲鏂�?"
        # name = u"鍙惰�?"

        infos = self.process_txt()

        for info in infos:
            name_pwds = self.generate_name(info[0])
            pwds.extend(self.weak_password())
            pwds.extend(name_pwds)

            if self.have_birthday:
                birth_pwds = self.generate_birth(info[1])
                pwds.extend(birth_pwds)
                pwds.extend(self.mix_name_birth(name_pwds, birth_pwds))
            if self.have_telnum:
                telnum_pwds = self.generate_telnum(info[2])
                pwds.extend(telnum_pwds)
                pwds.extend(self.mix_name_telnum(name_pwds,telnum_pwds))
            if self.have_qq:
                qq_pwds = self.generate_qq(info[3])
                pwds.extend(qq_pwds)
                pwds.extend(self.mix_name_qq(name_pwds,qq_pwds))
            if self.have_idnum:
                id_pwds = self.generate_idnum(info[4])
                pwds.extend(id_pwds)
                pwds.extend(self.mix_name_idnum(name_pwds,id_pwds))
            if self.have_lover:
                lover_pwds = self.lover_name(info[5])
                pwds.extend(lover_pwds)
                pwds.extend(self.mix_name_lover(name_pwds,lover_pwds))
            if self.have_special:
                special_pwds = self.special_num(info[6])
                pwds.extend(special_pwds)
                pwds.extend(self.mix_special(name_pwds,lover_pwds,special_pwds))
                
        f=open("password2.txt","w")
        for p in pwds:
            if len(p) >= 6 and len(p) <= 16:
                f.write(p)
                f.write("\n")
        f.close()
                    
                


if __name__ == "__main__":
    test = Password(int(argv[1]), int(argv[2]),int(argv[3]),int(argv[4]),int(argv[5]),int(argv[6]),int(argv[7]),argv[8])
    test.run()
