import random,math
from .common import number,integer,identifier,unique_ids

def quantile(values,p):
    ordered=sorted(values);index=(len(ordered)-1)*p;low=math.floor(index);high=math.ceil(index);return ordered[low]+(ordered[high]-ordered[low])*(index-low)
def run(data):
    pairs=data['pairs'];replicates=integer(data.get('replicates',1000),100,10000);seed=integer(data.get('seed',0),0,2**32-1);alpha=number(data.get('alpha',.05),.001,.5)
    if not 1<=len(pairs)<=10000:raise ValueError('size')
    unique_ids(pairs);blocks={}
    for row in sorted(pairs,key=lambda r:r['id']):
        a=number(row['a'],-1e12,1e12);b=number(row['b'],-1e12,1e12);key=identifier(row.get('block',row['id']));blocks.setdefault(key,[]).append(b-a)
    if len(blocks)>100:raise ValueError('block_limit')
    summaries=[(math.fsum(blocks[k]),len(blocks[k])) for k in sorted(blocks)];rng=random.Random(seed);values=[]
    for _ in range(replicates):
        selected=[summaries[rng.randrange(len(summaries))] for _ in summaries];values.append(math.fsum(x[0] for x in selected)/sum(x[1] for x in selected))
    delta=math.fsum(b-a for a,b in ((row['a'],row['b']) for row in pairs))/len(pairs)
    return {'paired_mean_b_minus_a':delta,'percentile_interval':[quantile(values,alpha/2),quantile(values,1-alpha/2)],'alpha':alpha,'blocks':len(blocks),'pairs':len(pairs),'replicates':replicates,'seed':seed,'more_than_one_resampling_unit':len(blocks)>1,'assumptions':'resample independent representative blocks; preserve within-block pairs; pooled observation mean with variable resampled block sizes; percentile interval is not a universal calibrated guarantee or causal effect'}
