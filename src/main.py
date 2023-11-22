
def createUI():
    '''
        COFFEE MACHINE UI:
        This function controls the appearance of the general window. The general format of the user interface
        will be split into several tabs. There will be tabs that allow uses to control physical paremeters 
        including Density, Mass and collision between the particles and a container. 
        
        tab 1 || tab 2 || tab 3 ||  ....
        ..............
        ..............
        ..............  
        
        Main tab:
        In the main tab users will be able to control physical parameters that affect particles in the system.
        There will also be default buttons that allow users the ability to select pre-defined liquids. By 
        selecting these liquids the physical parameters will change according to the best values that simulate that 
        particular liquid.
        
        General tab:
        The general tab controls the aesthetic of the particles, other physical parameters and general controls
        that affect individual particles in the system. For example, the particle radius and cluster radius and 
        particle colours. Manipulating the cluster radius affects the amount of particles that will be neighbour 
        to any particle in the system. There will also be user control over the number of simulated frames and 
        the frame rate. It is recommended that the frame rate stay close to 0.01 to achieve a realistic simulation.
        
        Orientation tab:
        This tab allows the user to specify the type of spawning orientation of the particles. This will
        control the shape to which they spawn when the user initially starts the simulation.
        
        Coffee tab:
        To allow the user more coffee specific controls, this tab includes drop-down menus of coffee roast levels. Each
        roast level automatically adapts the particle colour within the system. A user is also expected to press one
        of the coffee machines and choose a cup before they start the simulation. 
        
        The subsequent tabs will inform users of different instructions to best use the simulation, such as appropriate
        physical parameter values and steps to create an effective simulation.       
        
    '''
    if cmds.window('Coffee_Simulation', exists=True):
        cmds.deleteUI('Coffee_Simulation')
        
    winID = cmds.window('Coffee_Simulation', widthHeight=(500,430),resizeToFitChildren=True, sizeable=False) #creates the general window   

    newDirectory = queryDirectory() # queries the directory from the user when they start the program

    widgets = {} # creates a local dictionary to store values to pass into separate functions at a later stage
    
    tabs = cmds.tabLayout()
    tab1 = cmds.columnLayout(w=500,h=430,parent=tabs)
    tab2 = cmds.columnLayout(w=500,h=430,parent=tabs)
    tab3 = cmds.columnLayout(w=500,h=430,parent=tabs)
    tab4 = cmds.columnLayout(w=500,h=430,parent=tabs)
    tab5 = cmds.columnLayout(w=500,h=430,parent=tabs)
    tab6 = cmds.columnLayout(w=500,h=430,parent=tabs)
    tab7 = cmds.columnLayout(w=500,h=430,parent=tabs)
    
    # creation of different tab layouts 
    
    cmds.tabLayout(tabs,edit=True,
                    tabLabel=[(tab1,'Main'),(tab2,'General'),(tab3,'Orientation'),
                    (tab4,'Coffee'),(tab5,'Instructions'),(tab6,'Sim Instructions'),(tab7,'Coffee Instructions')])    
    cmds.setParent(tab1)
    
    ######################### TAB 1 #########################
    
    child1 = cmds.frameLayout(borderVisible=True, labelVisible=False, w=500,h=180)
    img = cmds.image(image=newDirectory + "artefacts//images//coffee_design_5.png", w=250, h=180) #loads the general image of the coffee machine
    
    cmds.setParent('..')    
    
    child2 = cmds.frameLayout('Liquid Parameters',w=500)
    title1 = cmds.rowColumnLayout(numberOfColumns=4, columnAttach=[(1,'both',30)])
    cmds.text('Type Of Liquid:')
    
    liquidType = 'Type Of Liquid'
    widgets[liquidType] = cmds.radioButtonGrp(numberOfRadioButtons=3, labelArray3=['Milk','Coffee','Water'], columnWidth=[(1,130),(2,130)], onCommand= lambda *pArgs: loadDefaultParams(widgets))
    # radio button group that allows users to specify default liquids and bypass customized options
    cmds.setParent('..')    
    cmds.setParent('..')    
    
    density, mass, viscosity, stiffness, surfaceTraction, buoyancy, ratioOfLossOfSpeed = 'Density', 'Mass', 'Viscosity', 'Stiffness', 'Delta', 'Buoyancy', 'RLOS'
    child4 = cmds.frameLayout('Physical Parameters',w=500)
    title2 = cmds.columnLayout(columnAttach = ('left',-85))
    widgets[density] = cmds.floatSliderGrp(label=density,minValue=0,maxValue=1500,value=998.2,field=True,precision=2, w=580)
    widgets[mass] = cmds.floatSliderGrp(label=mass,minValue=0,maxValue=10,value=0.1,field=True, step= 0.01, precision=3, w=580 )
    widgets[viscosity] = cmds.floatSliderGrp(label=viscosity,minValue=0,maxValue=10,value=3.5,field=True, w=580 )
    widgets[stiffness] = cmds.floatSliderGrp(label=stiffness,minValue=0,maxValue=10,value=3.0,field=True, w=580 )
    widgets[surfaceTraction] = cmds.floatSliderGrp(label=surfaceTraction,minValue=0,maxValue=0.5,value=0.0728,field=True,step=0.01,precision=4, w=580 )
    widgets[buoyancy] =  cmds.floatSliderGrp(label=buoyancy,minValue=0,maxValue=100,value=0,field=True, w=580 )
    widgets[ratioOfLossOfSpeed] = cmds.floatSliderGrp(label=ratioOfLossOfSpeed,minValue=0,maxValue=1,value=0.1,field=True, w=580 )      
    
    # physical parameter sliders that control the properties of particles within the system. These include mass, viscosity, surface traction (Delta), gas constant (stiffness)
    # all physical properties are passed into local widgets dictionary to be passed on into subsequent functions throughout the program
    
    cmds.setParent('..')
    cmds.setParent('..')
    
    child5 = cmds.rowLayout(numberOfColumns=3,columnWidth3=[160,160,160])
    button2 = cmds.button(label='Reset', command =  lambda *pArgs: resetProc1(widgets), w=165)
    button3 = cmds.button(label='Simulate', command = lambda *pArgs:startSimulation(widgets), w=165)
    button4 = cmds.button(label='Cancel',command= lambda *pArgs: cancelProc(winID),w=160)
    
    cmds.setParent(tab2)
    
    ######################### TAB 2 #########################
    
    numberOfS, radius, clusterRadius, spawnRadius, tankSize, particleColour = 'No. of Particles', 'Particle Radius', 'Cluster Radius', 'Spawn Radius', 'Tank Size', 'Particle Colour'
    child6 = cmds.frameLayout('Particle Properties',w=500)
    title3 = cmds.columnLayout(columnAttach = ('left',-50))
    widgets[numberOfS] = cmds.intSliderGrp(label=numberOfS,minValue=100,maxValue=10000,value=1000,field=True,w=540)
    widgets[radius] = cmds.floatSliderGrp(label=radius,minValue=0,maxValue=1,value=0.08,field=True,step=0.1,precision=4,w=540)
    widgets[clusterRadius] = cmds.floatSliderGrp(label=clusterRadius,minValue=0,maxValue=2,value=0.35,field=True,precision=2,w=540)
    widgets[spawnRadius] = cmds.floatSliderGrp(label=spawnRadius,minValue=0.5,maxValue=10,value=1.5,field=True,w=540)
    widgets[particleColour] = cmds.colorSliderGrp(label=particleColour,rgb=(0,0,1),w=540)
    # controls over the general aesthetic of the particles and their size.
    
    cmds.setParent('..')

    title5 = cmds.rowColumnLayout(numberOfColumns=2,columnAttach = (1,'both',10))
    cmds.image(image=newDirectory + "artefacts//images//uniform",h=70, w=240)
    cmds.image(image=newDirectory + "artefacts//images//particleRandom.png",h=70, w=230)
    
    #choosing whether to spawn the particles in a uniform or random distribution intially
    cmds.setParent('..')
    title6 = cmds.rowColumnLayout(numberOfColumns=2,columnAttach = (1,'both',10))
    widgets['Orientation'] = cmds.radioButtonGrp(numberOfRadioButtons=2, columnWidth2 = [240,240], labelArray2=['Uniform Distribution','Random Distribution'], 
                            onCommand= lambda *pArgs:selectOrientationType(widgets)) 
    
    cmds.setParent('..')
    cmds.setParent('..')
    
    child7 = cmds.frameLayout('Other Properties',w=500)
    title4 = cmds.rowColumnLayout(numberOfColumns=4, columnAttach=[(1,'both',10)])
    
    g, v = 'Gravity', 'Initial Velocity'
    cmds.text(g)
    widgets[g], widgets[v] = [], []
    gx = cmds.floatField(w=130)
    gy = cmds.floatField(v=-9.8,w=130)
    gz = cmds.floatField(w=130)
    widgets[g].append((gx,gy,gz))
    cmds.text(v)
    vx = cmds.floatField()
    vy = cmds.floatField(v=0.1)
    vz = cmds.floatField()
    widgets[v].append((vx,vy,vz))
    
    # variables that control other physical properties relevant to the system i.e gravity and initial velocity of the particles. 
    
    cmds.setParent('..')
    cmds.setParent('..')
    
    child8 = cmds.frameLayout('Animation Parameters',w=500)
    title5 = cmds.columnLayout(columnAttach = ('left',-50))
    numberOfF, timeDelta = 'No. of Frames', 'Time Difference'
    widgets[numberOfF] = cmds.intSliderGrp(label=numberOfF, minValue=0,maxValue=200,value=100,field=True, width=540)
    widgets[timeDelta] = cmds.floatSliderGrp(label=timeDelta, minValue=0.0,maxValue=1.0,value=0.01,field=True, step=0.01, precision=4, width=540)
    
    cmds.setParent('..')
    cmds.setParent('..')
    
    child8 = cmds.rowLayout(numberOfColumns=3,columnWidth2=[250,250])
    button5 = cmds.button(label='Reset', command =  lambda *pArgs: resetProc2(widgets), w=250)
    button6 = cmds.button(label='Cancel',command= lambda *pArgs: cancelProc(winID),w=250)
    
    cmds.setParent(tab3)
    
    ######################### TAB 3 #########################
    
    child9 = cmds.frameLayout('Spawning Orientation', w=500)
    title6 = cmds.rowColumnLayout(numberOfColumns=1)
    widgets['Orientation Grp'] = cmds.radioCollection('Orientation Grp')
    widgets['Orientation Type'] = []
    cmds.image(image=newDirectory + "artefacts//images//cylindrical1", w=495,h=170)
    cylindrical = cmds.radioButton('Cylindrical',label='Cylindrical',onCommand = lambda *pArgs:selectOrientationForm(widgets), collection=widgets['Orientation Grp'])
    cmds.image(image=newDirectory + "artefacts//images//uniform",w=495,h=165)
    bBox = cmds.radioButton('Bounding_Box',label='Bounding Box',onCommand = lambda *pArgs:selectOrientationForm(widgets), collection=widgets['Orientation Grp'])
    widgets['Orientation Type'].append((cylindrical,bBox))
    
    # allows the user to control the type of orientation to initially spawn the particles from. The options are a cylindrical or bounding box orientation. 
    # Links with the uniform and random distributions which provides users with 4 different types of spawning types:
        # uniform cylindrical distribution
        # random cylindrical distribution
        # uniform bounding box distribution
        # random bounding box distribution
        
    cmds.setParent('..')
    
    child10 = cmds.rowLayout(numberOfColumns=2,columnWidth2=[250,250])
    button10 = cmds.button(label='Delete Particles',command= lambda *pArgs: deleteGeometry('pSpheres'),w=250)
    button10 = cmds.button(label='Cancel',command= lambda *pArgs: cancelProc(winID),w=250)
    
    # other options to delete all particles within the system after the simulation has run
    cmds.setParent(tab5)
    
    ######################### TAB 4 #########################
    
    child11 = cmds.frameLayout('Default parameters',w=500)
    
    text1 = '''
    Water:
    ------------
    Density(rest): 998.2
    Mass(particle): 0.02
    Buoyancy Diffusion: 0
    Viscosity: 3.5
    Surface Tension: 0.0728
    Gas stiffness: 5
    Cluster Radius: 0.035
    ------------
    '''
    text2 = '''
    Milk:
    ------------
    Density(rest): 1036.2
    Mass(particle): 0.02
    Buoyancy Diffusion: 0
    Viscosity: 2.0
    Surface Tension: 0.0728
    Gas stiffness: 3
    Cluster Radius: 0.035
    ------------
    '''
    text3 = '''
    Coffee:
    ------------
    Density(rest): 1250
    Mass(particle): 0.021
    Buoyancy Diffusion: 0
    Viscosity: 10
    Surface Tension: 0.01 
    Gas stiffness: 2
    Cluster Radius: 0.035
    ------------
    '''
    child12 = cmds.paneLayout(configuration='vertical3')
    milk = cmds.text( text1,w=160, h=150)
    water = cmds.text(text2,w=160, h=150)
    coffee = cmds.text(text3,w=160, h=150)
    # text fields that explain to users the accurate physical parameters to input based on scientific experimentation and tested results.
    cmds.setParent('..')
    
    child13 = cmds.frameLayout('Properties Explained',w=500)
    
    text4 ='''
    -Increasing viscosity will make the fluid thicker.  
    
    -The model relies on finding particles that are within a radius of another particle, 
     this is known as the cluster radius. Increasing the cluster radius attracts more particles 
     closer to each other; and subsequently, the fluid will appear more dense.    
     
    -Surface tension controls the motion of particles when they collide with the ground. 
    
    -Gravity is directional. For a realistic simulation, gravity is -9.8 in the y-direction.    
    
    -Initial velocity and position controls the speed and position at which the fluid is moving. 
        
    -Ratio of loss of speed (RLOS) dictates the bounciness of the particles after collision.
     A greater ratio makes the particles bounce higher after contact with the ground.          

    '''
    cmds.text(text4,align='left', h=195)
    # Further instructions that outline methods to optimize the simulation by explaining the effects and meanings behind certain physical properties.
    cmds.setParent('..')
    
    title7 = cmds.rowLayout(numberOfColumns=2)
    button12 = cmds.button(label='Cancel',command= lambda *pArgs: cancelProc(winID),w=500)
    
    cmds.setParent(tab4)
    
    ######################### TAB 5 #########################
    
    child13 = cmds.frameLayout('Choose a machine',w=500)
    child14 = cmds.paneLayout(configuration='vertical2')
    cmds.iconTextButton(style='iconAndTextVertical',label='Model 1',image=newDirectory + "artefacts//images//coffee_machine", command = lambda *pArgs: loadObjProc(newDirectory + 'artefacts//MayaScene//' ,'coffee_machine','body'), w=240,h=200)
    cmds.iconTextButton(style='iconAndTextVertical',label='Model 2',image=newDirectory + "artefacts//images//second_coffee_machine.PNG", command = lambda *pArgs: loadObjProc(newDirectory + 'artefacts//MayaScene//','sec_coffee_machine','Componente_2_005'), w=240,h=200)    
   
    cmds.setParent('..')
    # allows the user to select from 2 types of machines by selecting machine icons
    child15 = cmds.frameLayout('Choose a cup',w=500)
    child16 = cmds.paneLayout(configuration='vertical3')
    cmds.iconTextButton(style='iconAndTextVertical',label='Mug',image=newDirectory + "artefacts//images//mug", command = lambda *pArgs: loadObjProc(newDirectory + 'artefacts//MayaScene//','mug','pCylinder3'),w=160,h=120)
    cmds.iconTextButton(style='iconAndTextVertical',label='Cup',image=newDirectory + "artefacts//images//cup", command = lambda *pArgs: loadObjProc(newDirectory + 'artefacts//MayaScene//','cup','cup_GEO'),w=165,h=120)
    cmds.iconTextButton(style='iconAndTextVertical',label='Glass',image=newDirectory + "artefacts//images//glass", command = lambda *pArgs: loadObjProc(newDirectory + 'artefacts//MayaScene//','glass','Tube001'),w=165,h=120)
    cmds.setParent('..')
    # allows the user to select from 3 different types of cups by selecting cup icons.
    child17 = cmds.rowLayout(numberOfColumns=1)
    widgets['Coffee Roast'] = cmds.optionMenu(w=500, changeCommand= lambda *pArgs: roastProc(widgets))
    cmds.menuItem(label='Coffee Roast')
    cmds.menuItem(label='light')
    cmds.menuItem(label='medium')
    cmds.menuItem(label='dark')
    cmds.menuItem(label='very dark')
    
    cmds.setParent('..')
    # different coffee types and roast options as drop-down menus for users to change the roast of their coffee; which will affect the colour of simulated particles.
    title9 = cmds.rowLayout(numberOfColumns=1)
    button14 = cmds.button(label='Cancel',command= lambda *pArgs: cancelProc(winID),w=500)
    
    cmds.setParent(tab6)
    
    ######################### TAB 6 #########################
    
    child17 = cmds.frameLayout('Simulation Instructions',w=500)
    
    text5 ='''
        - Simulations with more than 1600 particles and a cluster radius greater than
          0.35 can take up to an 30 minutes. If you wish to increase the number of 
          simulated particles, reducing the cluster radius will enable the simulation
          to run faster. 
          
        - A time step of 0.01 seconds is used in fluid simulations. Greater values will 
          have effects on the motion of the particles. If the time difference is too high
          particles will exhibit turbulent and erratic behaviour omnidirectionally. If
          this value is low, particles will move slower than a typical fluid. 
          
        - Increasing buoyancy will lead to fluctuating motion of particles. 
          If one wishes to simulate vapor atop the fluid, then increasing buoyancy will 
          create a gaseous effect.
          
        - If you wish to move the cup from  its initial location, or position the 
          particles away from the direction of the cup, please note that there will be 
          no collisions between particles and a container, so particles may be lost
          in 3D space.
          
        - A greater number of frames increases the simulation speed. If one wishes to
          use more particles in the simulation, there must be less frames to obtain
          quicker results. 
          
        - Within the maya interface, go to settings->preferences->Animation and make 
          sure that GPU override and parallel options are enabled. These settings 
          will cache the animation keyframes to a separate file and make the 
          simulation run smooothly.    
    '''
    cmds.text(text5, align='left')
    # text fields outlining possible limitations of the implementation of the program. 
    # Possible solutions to these problems are also defined, so users can create a realistic product.
    cmds.setParent('..')
    
    child18 = cmds.rowLayout(numberOfColumns=1)
    button16 = cmds.button(label='Cancel',command= lambda *pArgs: cancelProc(winID),w=500)
    
    cmds.setParent(tab7)
    
    ######################### TAB 7 #########################
    
    text6 = '''    
    - Set physical parameters in the 'main' tab. 
      To simulate a default liquid press on one of 
      the liquid types.
    - Choose particle, tank and time properties 
      under the 'General' tab.
    - If you wish to simulate coffee, there is an 
      optional coffee tab which controls coffee 
      specific functions such as roasting level 
      and coffee type.
    - Struggling to find the correct physical 
      parameters for a realistic simulation? The 
      Instructions tab outlines default physical 
      properties for generic liquids.
    - Finally press the Simulate button on the main 
      tab to start the simulation.     
   '''
    child19 = cmds.frameLayout('Machine Instructions', w=500)
    child20 = cmds.paneLayout(configuration='vertical2')
    cmds.image(image=newDirectory + 'artefacts//images//coffee_front_img.png', w=230,h=200)
    cmds.rowColumnLayout()
    cmds.text('Steps to create simulation:', font="boldLabelFont",align='center')
    cmds.text(text6,align='left',font="smallPlainLabelFont")  
    # text field outlining the specific steps to create the simulation by using the user interface.
    cmds.setParent('..')
    cmds.setParent('..')
    
    cmds.separator()
    
    text7 ='''**WARNING**
       If the number of particles exceeds 1000+ Maya will seldom crash. If the particles are 
       not spawning, or the program exhibits unchanging particle positions, 'Force Quit' Maya. '''
    cmds.text(text7,align='center',font="boldLabelFont") 
    
    cmds.separator()
    
    text8 = '''**NOTE**
        If the machine is moved or touched or deleted, the simulation result will be 
        affected. If a new machine is selected, remember to delete the geometry of a 
        previous machine. Please do not attempt to translate the machine or its contents to
        achieve realistic results. '''    
    # warnings and endnotes that outline things users shouldn't attempt to avoid the simulation crashing on them.     
    cmds.text(text8,align='center',font="boldLabelFont")  
    cmds.button(label='Cancel', command= lambda *pArgs: cancelProc(winID),w=500)
    
    cmds.showWindow(winID)

def cancelProc(winID,*pArgs):  
    # function to cancel the currently opened tab when the window is open
    print 'Cancelled'
    cmds.deleteUI(winID)        
   
def loadObjProc(filePath,name,objName,*pArgs):        
    '''
        function that allows .obj files to import into the current coffee scene in maya.
        
        filePath:    the file path to which the .obj files will be imported from
        name:    the abbrevated name given to .obj in the given filePath. E.g cup.obj will be cup
        objName:    the name of the .obj within the maya scene        
    '''      
    files = cmds.getFileList(folder=filePath, filespec='*.obj') # gets a list of all .obj files within the filePath directory
    if len(files)==0:
        print 'No files found in current directory' # if no files are found informs the user that 'No files are found' in the current directory
    else:
        for f in files: # for each file within the directory
            if f == (name + '.obj'):     # if the file matches the name within the maya scene, informs the user the file is found and tries to import it       
                print 'File found'  
                if cmds.objExists('Cup'): #  checks if an existing object by the name Cup exists within the scene and deletes it
                    print 'cup'
                    cmds.delete('Cup*')           
                cmds.file(filePath + f, i=True)  # action to import the .obj into the current maya scene               
                if objName=='body':                   
                    if cmds.objExists('Componente_2_005'):
                        cmds.delete('Componente_2_005') 
                        # if either one of the coffee machines exists in the current scene, it will delete that machine when another machine is loaded into the scene
                elif objName=='Componente_2_005':
                    obj = cmds.ls(objName) # if the second type of machine is selected it will list it into an object within the maya scene
                    cmds.move(-0.051,0.095,0.012,obj) #  moves the second machine object to specified coordinates within maya space
                    if cmds.objExists('body'):
                        cmds.delete('body')  #  deletes other type of machine if it currently exists in the scene
                    pass  
                else:
                    cmds.select(objName)
                    cmds.rename(objName, 'Cup')  # if one of the cup objects are imported into the scene, it renames all of them to Cup within the maya outliner.                                                                
                                
def queryDirectory(*pArgs):
    '''
        asks the user to enter the absolute file path towards the folder containing all the essential data for the program.
    '''
    currDirectory = cmds.promptDialog(title='Set current directory',
                                       message='Enter file path:',
                                       button = ['OK','Cancel'], defaultButton = 'OK',
                                       cancelButton='Cancel', dismissString='Cancel') # prompts the user to set the current directory
                                       # in windows system, the absolute file path should be '/' separated.
    newDirectory = ''
    if currDirectory == 'OK': # if the user selects the OK option, it will split the directory by '/' and replace every instance of it with '//'
       oldDirectory = cmds.promptDialog(q=True, text=True)
       for i in oldDirectory.split('\\'): # action to split the entered file path by '//'
           newDirectory += i + '//'
       return newDirectory # concatenates strings separated by '//' within entered file path into a separate string variable
       # returns string variable containing concatenated strings
    else:
       print 'No such file path exists in current directory.'  # if no such file path exists or is in the wrong format, informs users 'No such file path exists'
               
def loadDefaultParams(widgets, *pArgs):
    '''
        uses dictionary values from local widgets dictionary in UI, and changes
        physical parameters to default values by the specified type of liquid.
        widgets:    dictionary containing values to all UI controls in the program
    '''
    queryParams = cmds.radioButtonGrp(widgets['Type Of Liquid'],q=True,sl=True) # if one of the radioButtonGrp options for type of liquid is selected, execute an action
    if queryParams==1:
        cmds.floatSliderGrp(widgets['Density'], q=True, e=True, v=1036.2)
        cmds.floatSliderGrp(widgets['Mass'], q=True, e=True,  v = 0.1)
        cmds.floatSliderGrp(widgets['Viscosity'], q=True, e=True,  v = 2)
        cmds.floatSliderGrp(widgets['Stiffness'], q=True, e=True,  v = 5)
        cmds.floatSliderGrp(widgets['Delta'], q=True, e=True,  v = 0.0728)
        cmds.floatSliderGrp(widgets['Buoyancy'], q=True, e=True,  v = 0)
        cmds.floatSliderGrp(widgets['RLOS'], q=True, e=True,  v = 0.1)    
        cmds.colorSliderGrp(widgets['Particle Colour'],e=True,  rgbValue = (1,1,1))   # changes physical parameters to default parameters for realistic water simulations
    elif queryParams==2:
        cmds.floatSliderGrp(widgets['Density'], q=True, e=True,  v=1250.0)
        cmds.floatSliderGrp(widgets['Mass'], q=True, e=True,  v = 0.1)
        cmds.floatSliderGrp(widgets['Viscosity'], q=True, e=True,  v = 10)
        cmds.floatSliderGrp(widgets['Stiffness'], q=True, e=True,  v = 2)
        cmds.floatSliderGrp(widgets['Delta'], q=True, e=True,  v = 0.01)
        cmds.floatSliderGrp(widgets['Buoyancy'], q=True, e=True,  v = 0)
        cmds.floatSliderGrp(widgets['RLOS'], q=True, e=True,  v = 0.1)   
        cmds.colorSliderGrp(widgets['Particle Colour'], e=True,  rgbValue = (0.58,0.29,0))   # changes physical parameters to default parameters for realistic coffee simulations
    elif queryParams==3:
        cmds.floatSliderGrp(widgets['Density'], q=True, e=True,  v=998.2)
        cmds.floatSliderGrp(widgets['Mass'], q=True, e=True,  v = 0.1)
        cmds.floatSliderGrp(widgets['Viscosity'], q=True, e=True,  v = 3.5)
        cmds.floatSliderGrp(widgets['Stiffness'], q=True, e=True, v = 3)
        cmds.floatSliderGrp(widgets['Delta'], q=True, e=True,  v = 0.0728)
        cmds.floatSliderGrp(widgets['Buoyancy'], q=True, e=True,  v = 0)
        cmds.floatSliderGrp(widgets['RLOS'], q=True, e=True,  v = 0.1)   
        cmds.colorSliderGrp(widgets['Particle Colour'], e=True, rgbValue = (0,0,1))   # changes physical parameters to default parameters for realistic millk simulations

def resetProc1(widgets, *pArgs):
    '''
        resets buttons in the main tab to default values. Defaults are based on 
        physical parameters to simulate a realistic water.
        widgets:    dictionary containing values of all controls within the UI
    '''
    cmds.floatSliderGrp(widgets['Density'], q=True, e=True, v = 998.2)
    cmds.floatSliderGrp(widgets['Mass'], q=True, e=True, v = 0.1)
    cmds.floatSliderGrp(widgets['Viscosity'], q=True, e=True,  v = 3.5)
    cmds.floatSliderGrp(widgets['Stiffness'], q=True, e=True, v = 3)
    cmds.floatSliderGrp(widgets['Delta'], q=True, e=True,  v = 0.0728)
    cmds.floatSliderGrp(widgets['Buoyancy'], q=True, e=True, v = 0)
    cmds.floatSliderGrp(widgets['RLOS'], q=True, e=True, v = 0.1)    
    cmds.colorSliderGrp(widgets['Particle Colour'], e=True, rgbValue = (0,0,1)) 

def resetProc2(widgets,*pArgs):
    '''
        resets buttons within the General tab whenever the reset button is pressed by users.
        widgets:    dictionary containing values of all controls within the UI
    '''
    cmds.intSliderGrp(widgets['No. of Particles'], q=True, e=True, v = 1000)
    cmds.floatSliderGrp(widgets['Particle Radius'], q=True, e=True, v = 0.035)
    cmds.floatSliderGrp(widgets['Cluster Radius'], q=True, e=True,  v = 0.35)
    cmds.floatSliderGrp(widgets['Spawn Radius'], q=True, e=True, v = 1.5)
    cmds.floatSliderGrp(widgets['Tank Size'], q=True, e=True,  v = 6)
    cmds.intSliderGrp(widgets['No. of Frames'], q=True, e=True, v = 60)
    cmds.floatSliderGrp(widgets['Time Difference'], q=True, e=True, v = 0.01)  

def selectOrientationType(widgets,*pArgs):
    '''
        if the user selects an orientation type within the general tab,
        informs the user of the type of orientation they selected. Options are 
        uniform or random. 
        widgets:    dictionary containing values of all controls within the UI
    '''
    queryOrient = cmds.radioButtonGrp(widgets['Orientation'],q=True,sl=True) # checks which type of orientation was selected from the user
    if queryOrient == 1:
        print 'uniform orientation selected' # if the first radio button is selected, says 'uniform orientation selected'
    if queryOrient == 2:
        print 'random orientation selected' # if the second radio button is selected, says 'random orientation selected'

def selectOrientationForm(widgets,*pArgs):
    '''
        if an orientation type is selected within the orientation tab, enable or disable the radio 
        button that attaches to that specific orientation. E.g if cylindrical radio button is 
        selected, the corresponding 'Cylindrical radio button will be flagged as selected'
        widgets:    dictionary containing values of all controls within the UI
    '''
    queryGrp = cmds.radioCollection(widgets['Orientation Grp'],q=True,sl=True) # checks whether radio buttons corresponding to spawn orientation types are selected
    if queryGrp=='Bounding_Box':
        print 'Bounding Box orientation selected' #  informs the user if the spawn orientation type they selected is 'Bounding Box'
        cmds.radioCollection(widgets['Orientation Grp'],e=True,sl=widgets['Orientation Type'][0][1] ) #  if the first type is selected, flag the control of that type to selected
    if queryGrp=='Cylindrical': 
        print 'Cylindrical orientation selected'  #  informs the user if the spawn orientation type they selected is 'Cylindrical'  
        cmds.radioCollection(widgets['Orientation Grp'],e=True,sl=widgets['Orientation Type'][0][0] )   #  if the second type is selected, flag the control of that type to selected

def roastProc(widgets, *pArgs):
    '''
        changes the colour of the particles corresponding to a coffee roast level specified by the user.
        widgets:    dictionary containing values of all controls within the UI
    '''
    queryRoast = cmds.optionMenu(widgets['Coffee Roast'], q=True,v=True) # action to retrieve the value from the drop-down menu controlling coffee roast types.
    if queryRoast=='light': # if light roast is selected, change to light brown particle colour
        cmds.colorSliderGrp(widgets['Particle Colour'], e=True, enable=False, rgbValue=(0.7,0.4,0.1))
    if queryRoast=='medium':  # if medium is selected, change to brown particle colour
        cmds.colorSliderGrp(widgets['Particle Colour'], e=True, enable=False, rgbValue=(0.5,0.3,0.1))  
    if queryRoast=='dark':  # if dark is selected, change to dark brown particle colour
        cmds.colorSliderGrp(widgets['Particle Colour'], e=True, enable=False, rgbValue=(0.6,0.27,0.2))  
    if queryRoast=='very dark':  # if very dark is selected, change to very dark brown particle colour
        cmds.colorSliderGrp(widgets['Particle Colour'], e=True, enable=False, rgbValue=(0.35,0.25,0.2)) 

def deleteGeometry(groupName, *pArgs):
    '''
        if a group of objects exists by the given groupName, select and delete them
        groupName:    name of object to be deleted within the scene
    '''
    if cmds.objExists(groupName): # action to check whether an object by the given name exists in the scene
        cmds.select(groupName)
        cmds.delete()
                
def startSimulation(widgets, *pArgs):           
    '''
        starts the simulation using values specified by user within the program.
    '''
    params = {} # local dictionary that will contain values for each user specified parameter
    params['Density'] = cmds.floatSliderGrp(widgets['Density'], q=True, v=True)
    params['Mass'] = cmds.floatSliderGrp(widgets['Mass'], q=True, v=True)
    params['Viscosity'] = cmds.floatSliderGrp(widgets['Viscosity'], q=True, v=True)
    params['Stiffness'] = cmds.floatSliderGrp(widgets['Stiffness'], q=True, v=True)
    params['Delta'] = cmds.floatSliderGrp(widgets['Delta'], q=True, v=True)
    params['Buoyancy'] = cmds.floatSliderGrp(widgets['Buoyancy'], q=True, v=True)
    params['RLOS'] = cmds.floatSliderGrp(widgets['RLOS'], q=True, v=True)   
    params['No. of Particles'] = cmds.intSliderGrp(widgets['No. of Particles'], q=True, v=True)
    params['Particle Radius'] = cmds.floatSliderGrp(widgets['Particle Radius'], q=True, v=True)
    params['Cluster Radius'] = cmds.floatSliderGrp(widgets['Cluster Radius'], q=True, v=True)
    params['Spawn Radius'] = cmds.floatSliderGrp(widgets['Spawn Radius'], q=True, v=True)
    params['No. of Frames'] = cmds.intSliderGrp(widgets['No. of Frames'], q=True, v=True)
    params['Time Difference'] = cmds.floatSliderGrp(widgets['Time Difference'], q=True, v=True) 
    params['Particle Colour'] = cmds.colorSliderGrp(widgets['Particle Colour'], q=True, rgbValue=True)
    params['Gravity'] = [] # creates an empty list to append individual gravity values from based off user entries.
    params['Gravity'].append((cmds.floatField(widgets['Gravity'][0][0], q=True, v=True), cmds.floatField(widgets['Gravity'][0][1], q=True, v=True), 
                    cmds.floatField(widgets['Gravity'][0][2], q=True, v=True)))
    params['Initial Velocity'] = [] # creates an empty list to append individual initial position values from based off user entries.
    params['Initial Velocity'].append((cmds.floatField(widgets['Initial Velocity'][0][0], q=True, v=True), cmds.floatField(widgets['Initial Velocity'][0][1], q=True, v=True), 
                    cmds.floatField(widgets['Initial Velocity'][0][2], q=True, v=True)))
            
    if cmds.radioButton(widgets['Orientation Type'][0][1], q=True, sl=True):     # inspects whether the user has selected the given spawn orientation and distribution type, executing actions based off their selection            
        if cmds.radioButtonGrp(widgets['Orientation'], q=True, sl=True)==1: 
            deleteGeometry('pSpheres') # deletes any existing groups within the scene by the name of 'pSpheres'
            print 'uniform bounding box generating...'  # informs them of the type of spawn orientation and distribution type that they selected.             
            uniformBoxGenerator(params) # executes the corresponding code based off orientation entry.
        if cmds.radioButtonGrp(widgets['Orientation'], q=True, sl=True)==2:  
            deleteGeometry('pSpheres')
            print 'random bounding box generating...'              
            randomBoxGenerator(params) 
    if cmds.radioButton(widgets['Orientation Type'][0][0], q=True, sl=True):  
        if cmds.radioButtonGrp(widgets['Orientation'], q=True, sl=True)==1:  
            deleteGeometry('pSpheres')
            print 'uniform cylinder generating...'              
            uniformCylinderGenerator(params)
        if cmds.radioButtonGrp(widgets['Orientation'], q=True, sl=True)==2:
            deleteGeometry('pSpheres')
            print 'random cylinder generating...'                
            randomCylinderGenerator(params) 


def setMaterial(objName, materialType, colour):
   '''Assigns a material to the object 'objectName'

      objectName   : is the name of a 3D object in the scene
      materialType : is string that specifies the type of the sufrace shader, 
                     this can be any of Maya's valid surface shaders such as:
                     lambert, blin, phong, etc.
      colour       : is a 3-tuple of (R,G,B) values within the range [0,1]
                     which specify the colour of the material
      On Exit      : 'objName' has been assigned a new material according to the 
                     input values of the procedure, and a tuple (of two strings) 
                     which contains the new shading group name, and the new shader
                     name is returned to the caller
                     
     Code from Xiasong Yang ends here
	'''
   # create a new shading node
   setName = cmds.sets(name='_MaterialGroup_', renderable=True, empty=True)
   # create a new shading node
   shaderName = cmds.shadingNode(materialType, asShader=True)
   # change its colour
   cmds.setAttr(shaderName+'.color', colour[0], colour[1], colour[2], type='double3')
   # add to the list of surface shaders
   cmds.surfaceShaderList(shaderName, add=setName)
   # assign the material to the object
   cmds.sets(objName, edit=True, forceElement=setName)
                          
def randomBoxGenerator(widgets):
    '''
        randomly generate a cluster of spheres within a bounding radius
    '''
    pSphere, pSpheres = cmds.sphere(r=widgets['Particle Radius'],n='pSphere')[0], []  # initializes variables to create sphere and an empty list to contain the object names of pSphere instances.
    numSpheres = widgets['No. of Particles']
    for i in range(numSpheres):       
        pSphereInstName = 'pSphere_Inst' + str(i) # names the pSphere instances as pSphere instances 
           
        pos = [rd.uniform(-widgets['Spawn Radius'],widgets['Spawn Radius']) for j in range(3)] # randomly generates numbers that correspond to particle positions.
          
        pSphereInst = cmds.instance(pSphere, n=pSphereInstName)   # creates individual instances of pSpheres based off pSphere.
        setMaterial(pSphereInstName,'lambert', widgets['Particle Colour'])   # sets the colour of particles based on user entries.                     
        pSpheres.append(pSphereInst) # adds the particular instance of the particle into the pSpheres list. 
        #The list will ultimately contain each instance of the particle within the system:
            # [u'pSphereInst1,u'pSphereInst2,u'pSphereInst3....]
        cmds.move(pos[0],pos[1],pos[2],pSphereInst)
   
    cmds.select('pSphere') # selects the first sphere and deletes it.
    cmds.delete()  
    
    cmds.select('pSphere_Inst*')
    cmds.group(n='pSpheres') # groups all pSphere instances within the scene.
    
    animateFluid(widgets, pSpheres, numSpheres) # animates fluid based off user entries and number of Spheres specified by user.

def uniformBoxGenerator(widgets):
    '''
        randomly generate a cluster of spheres within a bounding radius
    '''
    numSpheres = widgets['No. of Particles']
    pSphere, pSpheres = cmds.sphere(r=widgets['Particle Radius'],n='pSphere')[0], [] # initializes variables to create sphere and an empty list to contain the object names of pSphere instances.
    x,y,z = int(widgets['No. of Particles']**1/100) , int(widgets['No. of Particles']**1/100) , int(widgets['No. of Particles']**1/100) # the number of spheres in each dimension is calculated by taking the cube root of the number of spheres.
    # calculations to compute x,y,z positions of where pSphere instances are to move to.
    spacing = widgets['Spawn Radius']/x # spacing between each particle is computed using the maximum spawn radius divided by the number of particles within a given dimension. 
    # i.e if 1000 particles are chosen, there should be a 10*10*10 orientation of particles, and that many particles should fit within the allowed spawn radius.
    
    ySpacing=0 #  creates different variables to hold spacing between particles in separate dimensions
    for k in range(y):
        ySpacing+=spacing 
        xSpacing = 0 # adds the spacing within each dimension by the pre-computed spacing based off the number of spheres in the system
        for j in range(x): 
            xSpacing+=spacing
            zSpacing=0
            for i in range(z):          
                pSphereInstName = 'pSphere_Inst' + str(i)    # names the pSphere instances as pSphere instances            
                pSphereInst = cmds.instance(pSphere, n=pSphereInstName)  # creates individual instances of pSpheres based off pSphere.
                pSpheres.append(pSphereInst)  
                cmds.move(xSpacing,ySpacing,zSpacing,pSphereInst) #  moves the particles to the positions specified by the spacing between each particle in a given dimension.
                zSpacing+=spacing 
    
    for i in pSpheres:
        setMaterial(i[0],'lambert', widgets['Particle Colour'])   # sets the colour of particles.
    
    cmds.select('pSphere') # selects the first sphere and deletes it.
    cmds.delete()    
    
    cmds.select('pSphere_Inst*')
    cmds.group(n='pSpheres') # groups all pSphere instances within the scene.                                            
    
    animateFluid(widgets, pSpheres, numSpheres) # animates fluid based off user entries and number of Spheres specified by user.

def uniformCylinderGenerator(widgets):
    '''
        creates a uniform cylinder of particles close to the size of the number of spheres the user specifies.
    '''
    numCircles = int(widgets['No. of Particles']**1/100)/2 
    height = int(widgets['No. of Particles']**1/100) # the number of particle tiers within the spawned cylinder should correspond to the permitted number of particles within a dimension
    #i.e if 1000 particles are used, the orientation will be 10*10*10 and there should be 10 tiers of particles.
    distBetweenS = 0.25 # fixed value to control the distance between spheres within a level of the cylinder.
    radius = 0.25
    increment = 0.25

    pSphere, pSpheres  = cmds.sphere(r=widgets['Particle Radius'],n='pSphere')[0], []   # creates the first particle and an empty list to contain all particle instance names.
    h=0
    for k in range(height):
        h+=increment #  increases the height of each tier of the cylinder by a fixed increment amount
        for j in range(numCircles): 
            
            numberOfCx = int(2.0*m.pi*j*radius/distBetweenS)  # using the radius of each particles, the distance between spheres and the circle formula 2*pi*radius, it will find the number of 
            # particles within a concentric circle in each level of the cylinder.
            for i in range(numberOfCx): # using the available number of particles, it will calculate their positions to circular orientation.
                    
                pSphereInstName = 'pSphere_Inst' + str(i)
                pSphereInst = cmds.instance(pSphere, n=pSphereInstName)  
                
                theta = m.radians(i*360.0/numberOfCx)
                xpos = j * radius * m.cos(theta) # calculates x position of each particle on each level using the angle between particles based on an available distance between particles.
                zpos = j * radius * m.sin(theta) # calculates z position of each particle on each level using the angle between particles based on an available distance between particles.
                pSpheres.append(pSphereInst) #  adds particle instances to pSpheres listt.
                cmds.move(xpos, h, zpos, pSphereInst)  # moves particle instances to individual positions.                          
    
    for i in pSpheres:
        setMaterial(i[0],'lambert', widgets['Particle Colour']) # sets the colour of particles. 
        
    cmds.select('pSphere') # selects the first sphere and deletes it.
    cmds.delete()  
    
    cmds.select('pSphere_Inst*') # groups all pSphere instances within the scene.
    cmds.group(n='pSpheres')
    
    length = len(pSpheres)
    animateFluid(widgets, pSpheres, length) # animates fluid based off user entries and number of Spheres specified by user.

def randomCylinderGenerator(widgets):
    '''
        creates a random distributin of particles in a cylindrical spawn orientation
    '''
    numCircles = int(widgets['No. of Particles']**1/100)/2 
    height = int(widgets['No. of Particles']**1/100)  # the number of particle tiers within the spawned cylinder should correspond to the permitted number of particles within a dimension
    #i.e if 1000 particles are used, the orientation will be 10*10*10 and there should be 10 tiers of particles.
    distBetweenS = 0.2 # fixed value to control the distance between spheres within a level of the cylinder.
    radius = 0.25
    increment = 0.25
    randomNess = 1.2
    pSphere, pSpheres  = cmds.sphere(r=widgets['Particle Radius'],n='pSphere')[0], []   # creates the first particle and an empty list to contain all particle instance names.
    h=0
    for k in range(height):
        h+=increment #  increases the height of each tier of the cylinder by a fixed increment amount
        for j in range(numCircles):            
            numberOfCx = int(2.0*m.pi*j*radius/distBetweenS)    # using the radius of each particles, the distance between spheres and the circle formula 2*pi*radius, it will find the number of 
            # particles within a concentric circle in each level of the cylinder.
            for i in range(numberOfCx):
                    
                pSphereInstName = 'pSphere_Inst' + str(i)
                pSphereInst = cmds.instance(pSphere, n=pSphereInstName)  
                
                theta = m.radians(i*360.0/numberOfCx)
                xpos = j * radius * m.cos(theta) * rd.uniform(-randomNess,randomNess) # calculates x position of each particle on each level using the angle between particles based on an available distance between particles.
                # xpos is multiplied by a randomNess constant to create a random outcome.
                zpos = j * radius * m.sin(theta) * rd.uniform(-randomNess,randomNess) # calculates z position of each particle on each level using the angle between particles based on an available distance between particles.
                # zpos is multiplied by a randomNess constant to create a random outcome.
                pSpheres.append(pSphereInst)    
                cmds.move(xpos, h* rd.uniform(-randomNess,randomNess), zpos, pSphereInst) # moves particle instances to individual positions. 
                    
    for i in pSpheres:
        setMaterial(i[0],'lambert', widgets['Particle Colour'])   # sets the colour of particles. 
                    
    cmds.select('pSphere') # selects the first sphere and deletes it.
    cmds.delete()  
    
    cmds.select('pSphere_Inst*') # groups all pSphere instances within the scene.
    cmds.group(n='pSpheres')
    
    length = len(pSpheres)
    animateFluid(widgets, pSpheres, length) # animates fluid based off user entries and number of Spheres specified by user.
        
def findPos(pSpheresPos):
    '''
        finds the position of particles generated
        pSpheresPos:    list containing instance names of each particle in system
        return:    a list within a list of coordinates indicating the position of every particle
    '''
    pos = [] #list will contain position coordinates of each particle
    for i in pSpheresPos:
        for j in i:
            obj = cmds.getAttr(j + '.translate') #finds the translation coordinates of every particle in system
            pos.append(obj) #  add coordinate values as list elements to pos list
    return pos            

def findNeighbour(clusterRadius,pSpheresPos,pSpheres,particleRadius):
    '''
    puts particles within a cluster group dictionary if within the specified
    cluster radius. 

    clusterRadius:    The cluster radius is the domain of each particle, which 
                        permits particles within the domain if they are less than or equal to the 
                        value.
    pSpherePos:    the coordinates of all particles in the system
    particleRadius:    the radius of each particle within the system
    pSpheres:    list containing instance names for each particle in system
    return:    returns cluster group dictionary of the clusterGroup name and any neighbouring
                particles within the domain of another particle will be within its clusterGroup.
    '''
    tmpGroup = {} # empty dictionary to hold key value pairs associating clusterGroups of particles within the radius of other particles
    for p in range(len(pSpheresPos)):
        name = 'clusterGroup' + str(p) # names the clusterGroup of each particle within the system
        coordsList = [] # temporary list to store x,y,z coordinates of particles into clusterGroup
        for j in range(p,len(pSpheresPos)):
            changeJ = [pSpheresPos[j][0][l] - pSpheresPos[p][0][l] for l in range(3)]
            dist_j = m.sqrt(changeJ[0]**2 + changeJ[1]**2 + changeJ[2]**2)-2*particleRadius # use to calculate the magnitude of subsequent particles by subtracting the positions
            # of previous particles within the list to that particle           
            if dist_j <= clusterRadius:
                coordsList.append(pSpheres[j][0]) # It will iterate through the positions of all particles, and if the distance between each neighbour particle to that particle is less than or equal to the cluster Radius, 
                #it will add the instance name of that particle to a cluster group
        for k in range(p):
            changeK = [pSpheresPos[k][0][l] - pSpheresPos[p][0][l] for l in range(3)] # use to calculate the distance of particles behind the current particle in list iteration
            dist_k = m.sqrt(changeK[0]**2 + changeK[1]**2 + changeK[2]**2)-2*particleRadius
            if dist_k <= clusterRadius: # if the magnitude of previous neighbour particles is less than or equal to the clusterRadius add the their instance name to the the particles clusterGroup
                coordsList.append(pSpheres[k][0])  
        tmpGroup[name] = coordsList 
    return tmpGroup

def findMatchingPairs(clusterGroup, pSpherePos):
    '''
        finds the matching particle position to clusterGroup particles

        clusterGroup:    dictionary containing every particle and its neighbours within a close proximity to that particle
                         i.e clusterGroup1:{[u'pSphere1],[u'pSphere7],u'pSphere13]...}
                         clusterGroup2:{[u'pSphere2],[u'pSphere9],u'pSphere18]...}
                                        ...
        pSpherePos:    list containing position values of every particle in system
        return:    if the clusterGroup key is equivalent to the particle number, return a list containing positions of particle instances
                   corresponding to that number.
    '''    
   
    objList = []
    for key, val in clusterGroup.items():
        for i in pSpherePos:
            for j in i:
                if j[12:] == key[12:]:
                    obj = cmds.getAttr(j + '.translate')
                    objList.append(obj)
    return objList

def findNeighbourPos(clusterGroup):
    '''
        finds the position of particles within each clusterGroup
       
        clusterGroup:    dictionary containing every particle and its neighbours within a close proximity to that particle
        return:    a list within a list of coordinates indicating the position of each particles
    '''            
    nPos = [] # empty list to contain neighbour particle x,y,z coordinates in cluster group
    for i in range(len(clusterGroup.items())):
        tempDist = []
        for j in range(len(clusterGroup.items()[i][1])):
            obj = cmds.getAttr(clusterGroup.items()[i][1][j] + '.translate') # gets the translation coordinates of each generated particle in clusterGroup vicinity
            tempDist.append(obj)
        nPos.append(tempDist)
    return nPos       

def findDistanceBetweenP(pos, match):
    '''
        finds the distance between particles and their neighbours
        
        pos:     position of each particle in system
        objL:    list of x,y,z positions of each particle in system
        return:    returns a list of distance coordinates between particle and its neighbours        
    '''
    distances = [] #list containing x,y,z distances of each particle to its cluster particles
    for i in range(len(pos)):
        tmp = []
        for j in range(len(pos[i])):
            dist = [pos[i][j][0][l] - match[i][0][l] for l in range(3)] # subtracts the distance position of each particle by its matching neighbours
            tmp.append(dist)#x,y,z coordinates of distances between particle to its neighbours
        distances.append(tmp)
    return distances
    
def findMagnitude(pos):
    '''
        finds magnitude between cluster particles in dictionary
       
        objList:    list to retain list of distance between particle and neighbour position
        clusterGroupDist:    dictionary of key value, clusterGroup to coordinates of particles in clusterGroup
        pSpherePos:    instance names of all particles in system
        pList:    temporary list containing x,y,z coordinates of distance between particles and neighbours
        return:    list of list containing distance between each particle to its neighbours        
    '''
    distL = []
    for i in range(len(pos)):
        tempList = []
        for j in range(len(pos[i])):
            mag = m.sqrt(pos[i][j][0]**2+pos[i][j][1]**2+pos[i][j][2]**2) # calculated magnitude using distance values in each direction
            tempList.append(mag) # list containing magnitude of each particle in a cluster neighbourhood
        distL.append(tempList)
    return distL 

def massDensity(mass,clusterRadius, mainRadius, magL, initialD, numParticles):
    '''
        computes the mass density of each particle within a cluster neighbourhood
        
        clusterRadius:    radius of particles within the neighbourhood
        magL:    the magnitude of distances between particles and their neighbours in 
                 a cluster
        return:    returns a list containing the mass density for each particle in system
    '''  
    densityL = [] #used to store mass density values of each particle
    for i in range(len(magL)):
        massD = 0 #intial mass is 0
        for j in range(len(magL[i])):
            wKernel =  (315/(64*m.pi*clusterRadius**9))*(clusterRadius**2 - magL[i][j]**2)**3 # weighting kernel for calculating mass density for each particle and its neighbours
            massD += initialD + mass*wKernel #temporarily storage variable of particle mass multiplied by kernel values
        densityL.append(massD)
    return densityL

def findPressure(mass,numParticles,mainRadius,initialD,massD,k):
    '''
        calculate the pressure acting on each particle in system
        
        pressureL:    list containing particle pressure values
        massD:    mass density of each particle
        initialD:    average density of particles throughout entire system
        mainRadius:    dimension of system size
        numParticles:    number of particles in system
        mass:    average mass of each particle
        return:    list of individual particle pressures
    ''' 
    pressureL = []
    for i in massD:
        pressureL.append(k*(i-initialD)) # list using calculated pressure values for each particle in system
    return pressureL
            
def findPressureForce(pressureL, massD, mass, clusterGroup, clusterRadius, positionV, magL):
    '''
        finds the pressure force between each particle and its neighbour
        
        pressureL:    list containing pressure fields of each particle
        mass:    average mass of each particle
        massD:    list of mass density field values of each particle
        clusterGroup:    dictionary containing clusterGroups and particles within them
        clusterRadius:    maximum radius for which a neighbouring particle is 
                          contained in that neighbourhood
        positionV:    list containing positions of cluster particles in neighbourhood
        magL:    list of magnitudes for each particle in cluster neighbourhood     
    '''  
    pressureForceL = []   #empty list to contain coordinates of pressure force vector for each particle in system
    for i in range(len(positionV)):
        pressureF, pFx, pFy, pFz = 0, 0, 0, 0
        for j in range(len(positionV[i])):
            index = int(clusterGroup.items()[i][1][j][12:]) # checks for the associated mass density and pressure coordinates associated to the particle name of each neighbour
            nPressure, nMass= pressureL[index], massD[index]  #indexing through the associated x,y,z mass densities and pressures of neighbours with that index 
            pressureF = mass*((pressureL[i]/massD[i]**2) + (nPressure/nMass**2))
            try:
                spiky = [(45.0/(m.pi*clusterRadius**6))*(positionV[i][j][k]/magL[i][j])*((clusterRadius-magL[i][j])**2) for k in range(3)]              
                pFx += pressureF*spiky[0]
                pFy += pressureF*spiky[1]
                pFz += pressureF*spiky[2] #temporary variables holding x,y,z coordinates of the pressureForce multiplied by the spiky kernel for each particle in system           
            except ZeroDivisionError: # if the particle has no neighbours, the initial position will be zero, and raises a ZeroDivisionError. Try and except is used to overcome that.
                pass
        pFx *= -mass
        pFy *= -mass
        pFz *= -mass # multiples the pressureForce variables by the mass in x,y,z directions of each particle
        pressureForceL.append((pFx,pFy,pFz))
    return pressureForceL

def findViscosityForce(clusterGroup, velL, massD, mass, viscosity, clusterRadius, magnitude):
    '''
        finds the viscosity force between particles in a cluster neighbourhood
        
        clusterGroup:    dictionary containing key value pairs of particles and there neighbours
        velL:    list of velocities of neighbouring particles in cluster group
        massD:    list of mass densities of particles in neighbourhood
        viscosity:    viscosity constant
        mass:    mass of each particle and its neighbours in a cluster
        clusterRadius:    region of affected particles in neighbourhood
        magnitude:    list of magnitudes of distances between particles and their neighbours
        return:    a list within a list of viscosity vector fields affecting each particle       
    '''   
    viscosityF = []
    for i in range(len(clusterGroup.items())):
        finalVisX, finalVisY, finalVisZ = 0, 0, 0 #initializing values for viscosity as zero
        for j in range(len(clusterGroup.items()[i][1])):
            try:
                index = int(clusterGroup.items()[i][1][j][12:]) #  finds the index of particle neighbours for each particle in the system.
                if index < len(clusterGroup.items()):                    
                    visF = [((velL[index][k] - velL[i][k])/ (massD[index]))*mass for k in range(3)] # variable the viscosity force acting between particles in the system
                    visKernel = (45.0/(m.pi*clusterRadius**6))*(clusterRadius - magnitude[i][j]) # calculating the viscosity kernel acting on each particle in the system
                    finalVisX += visF[0]*visKernel
                    finalVisY += visF[1]*visKernel
                    finalVisZ += visF[2]*visKernel # summation of viscosity force multipled by the viscosity kernel for each particle in each x,y,z direction
            except ZeroDivisionError:
                pass
        viscosityF.append((viscosity*finalVisX,viscosity*finalVisY,viscosity*finalVisZ))
    return viscosityF   

def findBuoyancy(g, massD, mass, b, initialD, mainRadius, numSpheres):
    '''
        finds buoyancy of each particle in system     
        
        mainRadius:    dimension of system size
        g:    gravity acting on particles   
        mass:    average mass of each particle
        massD:    list of mass densities of all particles system
        b:    buoyancy constant
        initialD:    average density of particles throughout entire system
        numSpheres:    number of particles in the system  
        return:    a list within a list of the buoyancy force
                     acting on each particle.      
    '''
    bForce = [[b*(i-initialD)*g[j] for j in range(3)] for i in massD] 
    # finds the buoyancy force acting on each particle based on the average mass density and gravity acting on the system
    return bForce
    
def findTractionF(mass,massD,mag,pos,clusterRadius,delta,clusterGroups):
    '''
        finds surface traction forces acting on particles interacting over collision surface.
        
        mass:    average mass of each particle
        massD:    list of mass densities of all particles system
        mag:    the magnitude of the distances between each particle and its neighbours
        pos:    the position of each particle in the system
        clusterRadius:    maximum radius for which a neighbouring particle is 
                          contained in that neighbourhood    
        delta:    surface traction constant
        clusterGroups:    dictionary containing key value pairs of particles and there neighbours
        return:    creates a list within a list of traction force vector values
                    acting on each particle in the system
    '''
    tForce = []
    for i in range(len(clusterGroups.items())):
        csX, csY, csZ, csLap, tmp = 0, 0, 0, 0, () # temporary values storing amounts to add normal forces by
        for j in range(len(clusterGroups.items()[i][1])):
            index = int(clusterGroups.items()[i][1][j][12:]) # finds the index of particle neighbours for each particle in the system. 
            poly6KernelGrad = [(-945.0/(32*m.pi*clusterRadius**9))*(pos[i][j][0][k]*((clusterRadius**2-mag[i][j]**2)**2)) for k in range(3)] 
            #implements the gradient of the poly6 kernel weighting function acting on each particle in system
            poly6KernelLap = (-945.0/(32*m.pi*clusterRadius**9))*((clusterRadius**2)-(mag[i][j]**2))*(3*(clusterRadius**2)-7*(mag[i][j]**2))
            #calculates the laplacian of the poly6 kernel weighting function acting on each particle in system
            csX += (mass/(massD[index]))*poly6KernelGrad[0]
            csY += (mass/(massD[index]))*poly6KernelGrad[1]
            csZ += (mass/(massD[index]))*poly6KernelGrad[2]
            csLap += (mass/(massD[index]))*poly6KernelLap # using temporary normal force values in each dimension, add them to normal forces acting 
            # on each particle in the system
        nMag = m.sqrt(csX**2+csY**2+csZ**2) #  calculate the magnitude of normal forces
        try:
            normalized = -delta*csLap
            tmp += (normalized*(csX/nMag),normalized*(csY/nMag),normalized*(csZ/nMag)) # adds the normal force coordinates to a tuple of all particles in
            #the system
            tForce.append(tmp)
        except ZeroDivisionError:
            pass # prevents ZeroDivisionErrors within the program
    return tForce

def findForces(pressureF, viscosityF,tractionF,bForce, mass, g):
    '''
        finds the sum of all forces per frame of animation
        
        pressureF:    list of pressure force coordinate values for particle
        viscosityF:    viscosity forces acting on each particle
        g:    gravitational forces acting on each particle in system
        mass:    mass of each particle
        return:    returns a list of coordinates retaining force values for each particle in system
    ''' 
    forceA =  [[(mass*g[j]) + viscosityF[i][j] + pressureF[i][j] + tractionF[i][j] + bForce[i][j] for j in range(3)] for i in range(len(viscosityF))] # list of forces of each particle in x,y,z directions
    return forceA    
    
def updateForce(mass,clusterGroups,clusterRadius,mainRadius,velL,mag,pos,dist,viscosity,g,b,k,delta,numSpheres,density,massD):
    '''
        updates forces based on particles in system and constant physical properties
        
        pSpheres:    list containing instances of all particles in system
        mainRadius:    size of the particle system
        clusterRadius:    radius for which particle will influence its neighbours
        mass:    mass of each particle
        g:    gravity force
        velL:    list containing x,y,z coordinates of each particle velocity
        numSpheres:    number of particles in system
        return:    a list of coordinates retaining the force acting on each particle x,y,z coordinates                        
    '''    
    pressure = findPressure(mass,numSpheres,mainRadius,density,massD,k) # pressure field coordinates for each particle in the cluster group
    pForce = findPressureForce(pressure, massD, mass, clusterGroups, clusterRadius, dist, mag) # finds the pressure force of each particle in the system
    visForce = findViscosityForce(clusterGroups, velL, massD, mass, viscosity, clusterRadius, mag) # finds viscosity of each particle
    tractionF = findTractionF(mass,massD,mag,pos,clusterRadius,delta,clusterGroups) # finds the surface traction force for each particle in the system
    bForce = findBuoyancy(g, massD, mass, b, density, mainRadius, numSpheres) #  finds the buoyancy force of each particle in the system
    allF = findForces(pForce,visForce,tractionF,bForce,mass,g) # calculates the sum of all forces acting on each particle in the system    
    return allF
    
def calXSPHVel(velL, clusterRadius, mass, massD, mag, clusterGroups): 
    '''
        calculate XSPH velocity correction for each particle
        velL:    the velocity vector of each particle  
        clusterRadius:   radius for which particle will influence its neighbours 
        mass:    average mass of each particle    
        massD:    list of mass densities of all particles system    
        mag:    the magnitude of the distances between each particle and its neighbours
        clusterGroups:    dictionary containing key value pairs of particles and there neighbours    
        return:    returns a list within a list of the velocities of each particle in the system
    '''
    newVel = []
    for i in range(len(clusterGroups.items())):
        XSPH, tmp = 0, [] # temporary veriables to hold updated XSPH velocity positions of each particle
        for j in range(len(clusterGroups.items()[i][1])):
            index = int(clusterGroups.items()[i][1][j][12:]) # finds the index of particle neighbours for each particle in the system. 
            wKernel =  (315/(64*m.pi*clusterRadius**9))*(clusterRadius**2 - mag[i][j]**2)**3 
            XSPH += 2*mass/(massD[i]+massD[index])*wKernel # summation of XSPH velocities for each particle in the system
        tmp.append((velL[i][0] + 0.1*XSPH,velL[i][1] + 0.1*XSPH,velL[i][2] + 0.1*XSPH))
        newVel.append(tmp) #adds the updated velocities from tmp list to a final list of particle velocities
    return newVel
                    
def animateFluid(widgets, pSpheres, numSpheres):
    '''
        animates the fluid based on user entered values
        
        widgets:    dictionary containing user controlled parameter values
        pSpheres:    list of all particle instances in the system
        numSpheres:    number of particles in the system.
    '''  
    
    g = widgets['Gravity'][0]
    clusterRadius = widgets['Cluster Radius']
    radius = widgets['Particle Radius']
    mainRadius = widgets['Spawn Radius']
    tankSize = 0.6
    mass = widgets['Mass']
    delta = widgets['Delta']
    density = widgets['Density']
    vis = widgets['Viscosity']
    b = widgets['Buoyancy'] 
    k = widgets['Stiffness'] 
    ratioOfLossOfSpeed = widgets['RLOS'] 
    velC = [widgets['Initial Velocity'][0]for k in range(numSpheres)] #sets the values of each user controlled parameter by passing in values from widgets dictionary
    initialPos = [[0.65,5.0,0.9] for k in range(numSpheres)]   
    frameInt = widgets['Time Difference']    
    amount,pro = 0, 0    
    cmds.progressWindow(	title='Fluid Simulation',
    					progress=amount,
    					status='Simulating: 0%',
    
    					isInterruptable=True, maxValue=widgets['No. of Frames']) # creates a progress window to show current frames of the simulation
				
    for i in range(1,widgets['No. of Frames']):
        
        pDist = findPos(pSpheres) # finds the coordinates of each particle         
        clusterGroups = findNeighbour(clusterRadius,pDist,pSpheres, radius) # creates a dictionary holding the particle cluster group as key and its associated particle neighbours
        pos = findNeighbourPos(clusterGroups) # finds the coordinates of each clusterNeighbour particle in the clusterGroup dictionary
        match = findMatchingPairs(clusterGroups,pSpheres) # compares clusterGroup name and particle names and returns the particle name associated to that cluster Group
        dist  = findDistanceBetweenP(pos,match) # finds the distance between the particle and its neighbours
        mag = findMagnitude(dist) # finds the magnitude of the distance between particles and their neighbours
        massD = massDensity(mass,clusterRadius,mainRadius, mag, density,numSpheres) # mass density of each particle in the clusterGroup        
        forces = updateForce(mass,clusterGroups,clusterRadius,mainRadius,velC,mag,pos,dist,vis,g,b,k,delta,numSpheres,density, massD) # updates the forces acting on each particle every frame                                         
        velC = [[velC[j][l] + frameInt*forces[j][l]/mass for l in range(3)] for j in range(numSpheres)] # calculates the forces influencing the velocity of each particle every frame
        XSPH = calXSPHVel(velC, clusterRadius, mass, massD, mag, clusterGroups)
        
        if i==1:
            posC = [[initialPos[j][l] + (pDist[j][0][l] + frameInt*(XSPH[j][0][l] + frameInt*(forces[j][l]/mass))) for l in range(3)] for j in range(numSpheres)]  # calculates the position of each particle every frame using calculated velocities and initial positions
        else:
            posC = [[(pDist[j][0][l] + frameInt*(XSPH[j][0][l] + frameInt*(forces[j][l]/mass))) for l in range(3)] for j in range(numSpheres)] # calculates the position of each particle every frame using calculated velocities         
        for k in range(len(posC)):
            
            if posC[k][0]<-tankSize:
                posC[k][0] = -tankSize+((-tankSize)-posC[k][0])
                velC[k][0] = -ratioOfLossOfSpeed*velC[k][0]
            if posC[k][0]>tankSize:
                posC[k][0] = -(posC[k][0]-tankSize)+tankSize
                velC[k][0] = -ratioOfLossOfSpeed*velC[k][0]
            if posC[k][1]<-tankSize:
                posC[k][1] = -tankSize+((-tankSize)-posC[k][1])
                velC[k][1] = -ratioOfLossOfSpeed*velC[k][1]
            if posC[k][2]<-tankSize:
                posC[k][2] = -tankSize+((-tankSize)-posC[k][2])
                velC[k][2] = -ratioOfLossOfSpeed*velC[k][2]
            if posC[k][2]>tankSize:
                posC[k][2] = -(posC[k][2]-tankSize  )+ tankSize 
                velC[k][2] = -ratioOfLossOfSpeed*velC[k][2]       # handles the collision between particle positions and the container                                 
                
            cmds.setKeyframe(pSpheres[k][0], attribute="tx", v=posC[k][0], t=[i], inTangentType="linear", outTangentType="linear")
            cmds.setKeyframe(pSpheres[k][0], attribute="ty", v=posC[k][1], t=[i], inTangentType="linear", outTangentType="linear")
            cmds.setKeyframe(pSpheres[k][0], attribute="tz", v=posC[k][2], t=[i], inTangentType="linear", outTangentType="linear") #animates the x,y,z positions of each particle every frame
            cmds.move(posC[k][0],posC[k][1],posC[k][2],pSpheres[k][0])
            
        cmds.refresh(f=True)            
        
        startTime = time.time()	
        
        # Check if the dialog has been cancelled
        if cmds.progressWindow( query=True, isCancelled=True ) :
            print 'Simulation terminated.'
            break
    
        # Check if end condition has been reached
        if cmds.progressWindow( query=True, progress=True ) >= widgets['No. of Frames'] :
            print 'Simulation successfully executed.'
            break
    
        amount += 1

        newTime = time.time() - startTime
        cmds.progressWindow( edit=True, progress=amount, status=('Frame: ' + `amount` ) )
        cmds.pause( seconds=newTime )
    
    cmds.progressWindow(endProgress=1)        
                
if __name__=='__main__':
    import maya.cmds as cmds
    import math as m
    import random as rd
    import sys
    import re
    import time
    createUI()      