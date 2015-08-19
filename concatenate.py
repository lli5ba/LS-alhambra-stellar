import numpy as np
import os

files_dir = "project"
files     = os.listdir(files_dir)

big_data  = None

count = 0
for f in files:
	if f[1]=='x' or f[2]=='x':
		
		data = np.genfromtxt( files_dir+'/'+f, dtype=str)
		print data.shape
		if big_data == None:
			big_data = data
	  	else:
			big_data = np.vstack([big_data, data])
		
		count = count+1
		print count

np.savetxt( files_dir+"/ALL.dat", big_data, fmt='%s',delimiter="   ", header='ID            Field   Pointing   CCD   RA         Dec      x          y          area   fwhm    stell   ell      a        b       theta   rk     rf       s2n        photoflag   F365W    dF365W   F396W    dF396W   F427W    dF427W   F458W    dF458W   F489W    dF489W   F520W    dF520W   F551W    dF551W   F582W    dF582W   F613W    dF613W   F644W    dF644W   F675W    dF675W   F706W    dF706W   F737W    dF737W   F768W    dF768W   F799W    dF799W   F830W    dF830W   F861W    dF861W   F892W    dF892W   F923W    dF923W   F954W    dF954W   J        dJ      H        dH      KS       dKS     F814W    dF814W   F814W_3arcs   dF814W_3arcs   F814W_3arcs_corr   nfobs   xray   PercW   Satur_Flag   Stellar_Flag   DupliDet_Flag   zb_1    zb_Min_1   zb_Max_1   Tb_1    Odds_1   z_ml    t_ml    Chi2     Stell_Mass_1   M_Abs_1   MagPrior   irms_F365W   irms_F396W   irms_F427W   irms_F458W   irms_F489W   irms_F520W   irms_F551W   irms_F582W   irms_F613W   irms_F644W   irms_F675W   irms_F706W   irms_F737W   irms_F768W   irms_F799W   irms_F830W   irms_F861W   irms_F892W   irms_F923W   irms_F954W   irms_J   irms_H   irms_KS   irms_F814W   irms_OPT_Flag   irms_NIR_Flag   AllWISE               RAJ2000       DEJ2000     eeMaj    eeMin    eePA    W1mag    W2mag    W3mag    W4mag   Jmag     Hmag     Kmag     e_W1mag   e_W2mag   e_W3mag   e_W4mag   e_Jmag   e_Hmag   e_Kmag   ID_x                  ccf    ex   var    qph    pmRA    e_pmRA   pmDE    e_pmDE   d2M     angDist  ')
