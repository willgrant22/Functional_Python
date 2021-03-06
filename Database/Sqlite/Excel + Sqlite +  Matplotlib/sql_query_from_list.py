#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import sqlite3, os
import matplotlib.pyplot as plt 
import numpy as np

def uTotalSales():
	db = 'data.db'
	conn = sqlite3.connect(f'{db}')
	cursor = conn.cursor()
	
	users = ['Jimmy', 'Timmy', 'Bob']
	userData=[]

	for user in users:
		transaction = f"SELECT TOTAL(SALEVAL) FROM DATA WHERE SDATE='July' AND USERNAME='{user}'"
		cursor.execute(transaction)
		userData.append(cursor.fetchone())
		
	userTuple = userData[0] + userData[1] + userData[2]

	labels = np.squeeze(np.array(users))
	sizes = np.squeeze(np.round([userTuple[0], userTuple[1], userTuple[2]], 3))
	colors = np.squeeze(np.array(['yellowgreen', 'lightcoral', 'lightskyblue']))

	explode = (0.0, 0.1, 0.0)

	def absolute_value(val):
	    a  = sizes[ np.abs(sizes - val/100.*sizes.sum()).argmin() ]
	    return f'${a}'

	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct=absolute_value,
        shadow=False, startangle=140)

	handles, labels = ax1.get_legend_handles_labels()
	legend = ax1.legend(handles, labels, loc="best")
	ax1.axis('equal') 
	title = ax1.set_title("Total sales for July (In dollars)") 
	plt.setp(title,size=16, weight="bold")
	plt.savefig('foo.svg', bbox_inches='tight')
	plt.show()

	conn.commit()
	conn.close()

uTotalSales()