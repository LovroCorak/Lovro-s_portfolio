# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:45:36 2025

@author: lovro
"""
import numpy as np
import pybullet as p
import pybullet_data
import time

p.connect(p.GUI) 
p.resetSimulation() 
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)  
p.setRealTimeSimulation(0) 

plane_id = p.loadURDF("plane.urdf", [0, 0, 0], [0, 0, 0, 1]) 
panda_id = p.loadURDF("franka_panda/panda.urdf", [0, 0, 0], [0, 0, 0, 1], useFixedBase=True)

obj_of_focus = panda_id  

print(p.getLinkState(panda_id, 0, computeForwardKinematics=True))

target_positions = [-0.5, -1, -1, 0.5, 0, 0, 0]


joint_indices = list(range(min(4, p.getNumJoints(panda_id))))

for step in range(100):
    p.setJointMotorControlArray(
        panda_id,
        joint_indices, 
        p.POSITION_CONTROL,
        targetPositions=target_positions[:len(joint_indices)],

    )


    focus_position, _ = p.getBasePositionAndOrientation(panda_id)
    p.resetDebugVisualizerCamera(
        cameraDistance=2,
        cameraYaw=0,
        cameraPitch=-40,
        cameraTargetPosition=focus_position,
    )
    p.stepSimulation()
    time.sleep(1. / 10.)
    #print(p.getLinkState(panda_id, 0, computeForwardKinematics=True))

p.disconnect()


