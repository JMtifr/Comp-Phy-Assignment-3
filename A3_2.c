#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <fftw3.h>
float f(float x) /* defining f(x) */
{ 
	if (x==0.0)
	{return 1.0;}
	else
	{return sin(x)/x;}
}
float an(float x) /* defining analytical function*/
{ if (fabs(x)<=1.0)
	{return sqrt(M_PI/2.0);}
	else
	{return 0.0;}}
/*-------------------------------------------------------------------------*/
int main()
{ 
	int n=1024,i;
	float x_min,x_max,dx,w[n],k[n],anlyt[n];
	fftw_complex y_x[n],y_k[n];
	fftw_plan p;
	p=fftw_plan_dft_1d(n,y_x,y_k,FFTW_FORWARD,FFTW_ESTIMATE);
	
	x_min=-30.0*M_PI;x_max=30.0*M_PI;
	dx=(x_max-x_min)/(float)(n-1);
/* creating [y(x)] and [k] arrays */	
	for (i=0;i<n;i++)
	{if(i<n/2){ /* creating k array using periodicity condition */
		k[i]=M_PI*2.0*(float)i/(float)n/dx ;}
		else
		{k[i]=M_PI*2.0*(float)(i-n)/(float)(n)/dx;}
	y_x[i][0]=f(x_min+dx*(float)i); y_x[i][1]=0.0; /* evaluating points for dft = f(x) */	
	}
/*-------------------------------------------------------------------------*/	
 /*----------------------- Calculating dft  and printing in file-----------------------------*/
	FILE*fptr;
	fptr=fopen("A3_2.csv","w");
	fftw_execute(p); // dft (unnormalised)
	for(i=0;i<n;i++) /* evaluating ft */
	{ w[i]=dx*sqrt(1.0/2.0/M_PI)*(cos(-x_min*k[i])*y_k[i][0]-sin(-x_min*k[i])*y_k[i][1]);
		anlyt[i]=an(k[i]);}
	
		for (i=n/2;i<n;i++)
		{
		fprintf(fptr,"%f, %f, %f\n", k[i],w[i],anlyt[i]);}
		for (i=0;i<n/2;i++)
		{
		fprintf(fptr,"%f, %f, %f\n", k[i],w[i],anlyt[i]);}
		fclose(fptr);
 /* -----------------------------------------------------------------------*/
	fftw_destroy_plan(p);
	return 0;
}

	
