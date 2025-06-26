import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def plot_correlation(log1, log2, wp, d1=None, d2=None, step:int=5, figsize=(5,7), wspace=5, colors=['C0', 'C1'], cmap='Accent'):
    colormap = mpl.colormaps.get_cmap(cmap)
    lb = np.min([log1.min(), log2.min()])-0.5
    depth = np.arange(log1.shape[-1])
    d1 = depth if d1 is None else d1
    d2 = depth if d2 is None else d2
    p, q = wp[:,0], wp[:,1]

    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    
    ax.plot(log1,          d1-np.min(d1), c=colors[0])
    ax.plot(log2 + wspace, d2-np.min(d2), c=colors[1])
    
    for i in range(0, len(p)-step, step):
        
        # intervals for log on the left:
        depth1_base = d1[p[i]]-np.min(d1)
        depth1_top = d1[p[i+step]]-np.min(d1)
        if p[i+step] < p[i]:
            mean_log1 = np.mean(log1[p[i+step]: p[i]])
            fillcolor = colormap(mean_log1)
            x = [lb, wspace-1, wspace-1, lb]
            y = [depth1_base, depth1_base, depth1_top, depth1_top]
            plt.fill(x, y, color=fillcolor)
            plt.plot([0, 0], [depth1_base, depth1_top], c='k', lw=0.5, ls=':')
        else:
            mean_log1 = log1[p[i]]

        # intervals for log on the right:
        depth2_base = d2[q[i]]-np.min(d2)
        depth2_top = d2[q[i+step]]-np.min(d2)
        if q[i+step] < q[i]:  
            mean_log2 = np.mean(log2[q[i+step]: q[i]])
            fillcolor = colormap(mean_log2)
            x = [wspace, wspace+wspace, wspace+wspace, wspace]
            y = [depth2_base, depth2_base, depth2_top, depth2_top]
            plt.fill(x, y, color=fillcolor)
            plt.plot([wspace, wspace], [depth2_base, depth2_top], c='k', lw=0.5, ls=':')
        else:
            mean_log2 = log2[q[i]]

        # intervals between the two logs:
        if (p[i+step] < p[i]) or (q[i+step] < q[i]):
            mean_logs = (mean_log1 + mean_log2)/2
            fillcolor = colormap(mean_logs)
            x = [wspace-1, wspace, wspace, wspace-1]
            y = [depth1_base, depth2_base, depth2_top, depth1_top]
            plt.fill(x, y, color=fillcolor)
            plt.plot([wspace-1, wspace-1], [depth1_top, depth1_base], c='k', lw=0.5, ls=':')

    plt.xticks([])
    plt.xlim(lb, wspace*2)
    plt.yticks(np.arange(0, len(depth), 20), depth[::20])
    plt.ylabel('depth (ft)')
    plt.ylim(0, len(d1))
    plt.gca().invert_yaxis()
    return None