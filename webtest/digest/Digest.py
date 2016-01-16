import re


class Digest():
    enzymelist = []
    selectedenzyme = []
    def __init__(self, elist):
        """initiation with enzyme list, which is a list of all enzymes from database.
            the formation is [[name, amount, digest, start_pos],[],[]...]
            the data type is [str, int, str, str]"""
        self.enzymelist = elist

    def selectenzyme(self, chosen = [] , allselect = False):
        """to select the chosen enzyme
            chosen is a list of int, or a allselect flag will choose all enzymes."""
        if allselect:
            self.selectedenzyme = self.enzymelist
        else:
            for i in chosen:
                self.selectedenzyme.append(self.enzymelist[i])

    def digest(self,seq):
        """ Main digest method.
            This method digest the sequence with each enzyme."""
        result = []
        seq = self.seq_formation(seq)
        for enzyme in self.selectedenzyme:
            pos = []
            if enzyme[1] == 1:
                pattern = re.compile(enzyme[2])
                m = pattern.search(seq)            
                while(m):
                    start = m.start()
                    pos.append(str(start+int(enzyme[3])))
                    m = pattern.search(seq,m.start()+1)
            else:
                re_l = enzyme[2].split(',')
                pos_l_t = enzyme[3].split(',')
                pos_l = []
                for i in pos_l_t:
                    pos_l.append( int(i))
                for i in range(len(re_l)):
                    pattern = re.compile(re_l[i])
                    m = pattern.search(seq)
                    while(m):
                        start = m.start()
                        pos.append(str(start+pos_l[i]))
                        m = pattern.search(seq,m.start()+1)
                pos = list(set(pos)).sort()

            result.append(pos)

        return result
    
    def seq_formation(self,seq):
        """ get the input sequence and try to parse it if it is in FASTA format"""
        seq = seq.upper()
        l = seq.split('\n')
        if seq[0] == '>':
            seq = ''.join(l[1:])
        else:
            seq = ''.join(l)
        return ''.join(seq.split())

    def is_legal(self,seq):
        """ if the input sequence containing illegal characters,
            this method will return False."""
        pattern = re.compile('[^ACDEFGHIKLMNPQRSTVWY]')
        match = pattern.match(seq)
        if match:
            return False
        else:
            return True
    def output_seq(self,seq):
        """ prepare the output formation of the sequence
            the sequence will be split to 10 aa size and a serial number will be added
            the return type is a like [[a1], [b1], [a2], [b2] ...]
            [aX] is a list of int and [bX] is a list of str"""
        result_seq = []
        result_num = []
        output_seq = []
        output_num = []
        for i in range(0,len(seq)-10,10):
            seq_temp = ' '
            seq_temp += seq[i:i+10]
            result_seq.append(seq_temp)
            result_num.append(i+10)
        if len(seq) % 10 != 0:
            seq_temp = ' '
            seq_temp += seq[len(seq)/10 *10:len(seq)]
            result_seq.append(seq_temp)
            result_num.append(len(seq))
        
        for i in range(0,len(result_seq)-6,6):
            temp = []
            for j in range(i,i+6):
                temp.append(result_num[j])
            output_num.append(temp)
            temp = []
            for j in range(i,i+6):
                temp.append(result_seq[j])
            output_seq.append(temp)
            
        temp = []
        for j in range((len(result_seq)-1)/6 *6,len(result_seq)):
            temp.append(result_num[j])
        output_num.append(temp)
        temp = []
        for j in range((len(result_seq)-1)/6 *6,len(result_seq)):
            temp.append(result_seq[j])
        output_seq.append(temp)
        output = []
        for i in range(len(output_num)):
            output.append(output_num[i])
            output.append(output_seq[i])
        return output

# for test
if __name__ == '__main__':
    import model
    el = model.enzymes()
    chosen = []
    #s = 'qweaaaadssss22aaaadssss333aaaadssss44waaaadssssr'
    s = raw_input()
    o = Digest(el.enzyme)
    o.selectenzyme(allselect=True)
    a = o.digest(s.upper())
