# %%add_to PostProcess
from RunOpenFOAMv4 import PostProcess


def diffuser(self, ind):
    def main():
        # OpenFOAM file generation
        os.system('touch cases/gen%i/ind%i/g%ii%i.OpenFOAM'
                  % (self.gen, ind, self.gen, ind))
        ### paraview batch mode ###
        L = self.x[ind, 0]
        theta = self.x[ind, 1]
        L_diff = 4 + L * np.cos(np.deg2rad(theta))
        print('L_diff: %f' % L_diff)
        os.system('pvbatch paraviewPostProcess.py %i %i %.8f'
                  % (self.gen, ind, L_diff))
        ## analysis data file in python ##
        PR, Ma = meanCompValue(ind)
        obj_i = [PR, Ma]
        return obj_i

    def meanCompValue(ind):
        def main():
            # Case parameters
            Uinf = 590  # m/s
            Tinf = 216  # K
            Pinf = 19330  # Pa
            gamma = 1.4

            # Upstream conditions
            Minf = Uinf / np.sqrt(gamma * 287 * Tinf)
            P0inf = Pinf * (1 + (gamma - 1) / (2) * Minf ** 2) ** ((gamma) / (gamma - 1))

            # The expected header of the file is
            header = ['p', 'U_x', 'U_y', 'U_z', 'T', '\alpha_t', '\varepsilon', 'k', '\nu_t', '\rho', 'vtk', 'arc', 'x',
                      'y', 'z']

            # Read the data file
            data = np.genfromtxt('./cases/gen%i/ind%i/plotOverLineData.csv' % (self.gen, ind), skip_header=1,
                                 delimiter=',')

            #########################################################
            #                   MAIN FUNCTION                       #
            #########################################################
            # Figures preamble
            plt.style.use('seaborn-deep')
            plt.style.use('classic')
            matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler('color',
                                                                       ['#0072B2', '#009E73', '#D55E00', '#CC79A7',
                                                                        '#F0E442', '#56B4E9'])
            matplotlib.rcParams['axes.linewidth'] = 1.3
            matplotlib.rcParams['lines.linewidth'] = 1.3
            matplotlib.rc('text', usetex=True)
            matplotlib.rcParams['text.latex.preamble'] = [r"\usepackage{amsmath}"]
            matplotlib.rcParams.update({'font.size': 8})

            # Analyze the length of the header before going on
            if len(header) == len(np.loadtxt('./cases/gen%i/ind%i/plotOverLineData.csv'
                                             % (self.gen, ind),
                                             dtype='str', delimiter=',')[0, :]):
                # Velocity magnitude computation
                Umag = np.sqrt(data[:, 1] ** 2 + data[:, 2] ** 2 + data[:, 3] ** 2)
                # Mach computation
                M = Umag / np.sqrt(gamma * 287 * data[:, 4])
                # Velocity magnitude plotting
                velocityPlot()
                # Total pressure computation
                P0 = data[:, 0] * (1 + (gamma - 1) / (2) * M ** 2) ** ((gamma) / (gamma - 1))
                # Total pressure plotting
                pressurePlot()
                # File saving of the values of the simulation
                np.savetxt('./cases/gen%i/data/FITg%ii%i.txt' % (self.gen, self.gen, ind),
                           np.array([np.nanmean(P0) / P0inf, np.nanmean(M)]))

                PR = np.nanmean(P0) / P0inf
                Ma = np.nanmean(M)
                return PR, Ma
            else:
                raise ValueError('Incorrect .csv file!')

        def pressurePlot():
            # Total pressure plotting
            fig, ax = plt.subplots(1, figsize=(8, 6))
            ax.plot(P0 / 1e3, 'r', lw=2, label=r'$P$')
            ax.plot(np.nanmean(P0) / 1e3 * np.ones(len(P0)), 'r:', lw=2, label=r'$\mu_{P}$')
            ax.plot([0, len(data)], [P0inf / 1e3, P0inf / 1e3], 'k-.', lw=1.5, label=r'$P_{\infty,0}$')
            ax.set_xlabel(r'$y\ (m)$', fontsize=20)
            ax.set_ylabel(r'$P\ (kPa)$', fontsize=20)
            ax.legend(fontsize=16, loc='lower left')
            ax.set_xlim([0, len(data)])
            ax.set_xticks([0, 0.5 * len(data), len(data)])
            ax.set_ylim([1, 180])
            ax.set_xticklabels([r'$0.10$', r'$0.45$', r'$0.80$'])
            ax.tick_params(axis='both', labelsize=18)
            ax.set_title('Total pressure', fontsize=26)
            plt.savefig('./cases/gen%i/data/Pg%ii%i.png' % (self.gen, self.gen, ind), bbox_inches='tight', dpi=200)

        def velocityPlot():
            # Velocity magnitude plotting
            fig, ax = plt.subplots(1, figsize=(8, 6))
            ax.plot(M, 'b', lw=2, label=r'$Ma$')
            ax.plot(np.nanmean(M) * np.ones(len(data[:, 2])), 'b:', lw=2, label=r'$\mu_{Ma}$')
            ax.set_xlabel(r'$y\ (m)$', fontsize=20)
            ax.set_ylabel(r'$Ma$', fontsize=20)
            ax.legend(fontsize=16, loc='lower left')
            ax.set_xlim([0, len(data)])
            ax.set_xticks([0, 0.5 * len(data), len(data)])
            ax.set_ylim([0.25, 3])
            ax.set_xticklabels([r'$0.10$', r'$0.45$', r'$0.80$'])
            ax.tick_params(axis='both', labelsize=18)
            ax.set_title('Mach number', fontsize=26)
            plt.savefig('./cases/gen%i/data/Mag%ii%i.png' % (self.gen, self.gen, ind), bbox_inches='tight', dpi=200)

        main()

    obj_i = main()
    return obj_i


PostProcess.diffuser = diffuser
