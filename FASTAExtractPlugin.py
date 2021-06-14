import PyPluMA

class FASTAExtractPlugin:
    def input(self, filename):
       params = open(filename, 'r')
       self.parameters = dict()
       for line in params:
          contents = line.strip().split('\t')
          self.parameters[contents[0]] = contents[1]
       self.fasta = PyPluMA.prefix()+"/"+self.parameters["fasta"]
       self.start = int(self.parameters["start"])  #Assuming indexing is from 1
       self.end = int(self.parameters["end"])  #Assuming indexing is from 1

    def run(self):
       fastafile = open(self.fasta, 'r')
       self.header = fastafile.readline().strip()
       self.header += " extracted by PluMA, region "+str(self.start)+"-"+str(self.end)
       DNA = ''
       for line in fastafile:
           DNA += line.strip()
       self.region = DNA[self.start-1:self.end]


    def output(self, filename):
       outfile = open(filename, 'w')
       outfile.write(self.header+"\n")
       outfile.write(self.region)
