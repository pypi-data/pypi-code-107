import collections

try:
    from utils import revCompIterative
    from utils import sortORFs
except ImportError:
    from ORForise.utils import revCompIterative
    from ORForise.utils import sortORFs


def GeneMark_HA(tool_pred, genome):
    geneMark_HA_ORFs = collections.OrderedDict()
    genome_size = len(genome)
    genome_rev = revCompIterative(genome)
    with open(tool_pred, 'r') as GeneMark_HA_input:
        for line in GeneMark_HA_input:
            line = line.split()
            if len(line) >= 9 and "CDS" in line[5]:
                start = int(line[6])
                stop = int(line[7])
                strand = line[9]
                if '-' in strand:  # Reverse Compliment starts and stops adjusted
                    r_start = genome_size - stop
                    r_stop = genome_size - start
                    startCodon = genome_rev[r_start:r_start + 3]
                    stopCodon = genome_rev[r_stop - 2:r_stop + 1]
                elif '+' in strand:
                    startCodon = genome[start - 1:start + 2]
                    stopCodon = genome[stop - 3:stop]
                po = str(start) + ',' + str(stop)
                orf = [strand, startCodon, stopCodon]
                geneMark_HA_ORFs.update({po: orf})

    geneMark_HA_ORFs = sortORFs(geneMark_HA_ORFs)
    return geneMark_HA_ORFs
