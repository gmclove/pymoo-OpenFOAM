#%%add_to PostProcess
def cylinder(self, ind):
    def main():
        sigmaX, sigmaY = forcePlotAnalysis(ind)
        obj_i = [sigmaX, sigmaY]
        return obj_i
    def forcePlotAnalysis(self, ind):
        #os.system('postProcess -latestTime')
        def main():
            # Read the file efficientyly
            s = open('./cases/gen%i/ind%i/postProcessing/forces/0/forces.dat' %(self.gen, ind)).read().replace('(',' ').replace(')',' ').replace('\t',' ')
            forces = np.genfromtxt(io.BytesIO(s.encode()))

            # GET
            timestp40 = int(np.argwhere(forces[:,0]>40)[0])

            matFX = np.invert(forces[timestp40:,1] > forces[-1,1])
            logicFX = np.logical_xor(matFX[0:-2],matFX[1:-1])
            if len(np.argwhere(logicFX))%2 == 1:
                fx = int(np.argwhere(logicFX)[1])
            else:
                fx = int(np.argwhere(logicFX)[0])

            matFY = np.invert(forces[timestp40:,2] > forces[-1,2])
            logicFY = np.logical_xor(matFY[0:-2],matFY[1:-1])
            if np.sum(logicFY) == 0:
                fy = timestp40
            else:
                if len(np.argwhere(logicFY))%2 == 1:
                    fy = int(np.argwhere(logicFY)[1])
                else:
                    fy = int(np.argwhere(logicFY)[0])


            sigmaX = np.std(forces[timestp40+fx:,1]+forces[timestp40+fx:,4])
            sigmaY = np.std(forces[timestp40+fy:,2]+forces[timestp40+fy:,5])

            #displayData(ind, sigmaX, sigmaY)
            #saveData(sigmaX, sigmaY)

            return sigmaX, sigmaY

        def saveData(self, ind, sigmaX, sigmaY):
            def saveFig():
                # Save figure
                fig, (ax1) = plt.subplots(1, figsize=(10,8))

                ax1.plot(forces[timestp40+fx:,0],forces[timestp40+fx:,1]+forces[timestp40+fx:,4],'b',linewidth=2,label='Pressure Force X')             # ax1.plot(forces[timestp40+fx:,0],np.mean(forces[timestp40+fx:,1])*np.ones(len(forces[timestp40+fx:,0])),':b',linewidth=1)
                ax1.plot(forces[timestp40+fy:,0],forces[timestp40+fy:,2]+forces[timestp40+fy:,5],'g',linewidth=2,label='Pressure Force Y')
                # ax1.plot(forces[timestp40+fy:,0],np.mean(forces[timestp40+fy:,2])*np.ones(len(forces[timestp40+fy:,0])),':g',linewidth=1)
                ax1.set_xlabel('Time (s)', fontsize=16)
                ax1.set_ylabel(r'Force ($N$)', fontsize=16)
                ax1.legend(loc='lower left', fontsize=16)
                ax1.tick_params(labelsize=14)
                ax1.set_ylim([-0.3,0.3])
                ax1.set_xlim([0,150])
                # Save figure
                fig, (ax1) = plt.subplots(1, figsize=(10,8))
                plt.savefig('./cases/gen%i/data/OSCg%ii%i.png' %(self.gen, self.gen, ind), bbox_inches='tight', dpi=100)
            def saveText():
                # Save fitness to text file
                np.savetxt('./cases/gen%i/data/FITg%ii%i.txt' %(self.gen, self.gen, ind),
                           np.array([sigmaX, sigmaY]))

            #os.system('mkdir cases/gen%i/data' % self.gen)
            os.mkdir('./cases/gen%i/data' %self.gen)
            saveFig()
            saveText()
        main()
    obj_i = main()
    return obj_i

PostProcess.cylinder = cylinder