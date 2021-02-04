#include <stdio.h>
#include <math.h>

int main()
{
	float x, y;

	for ( x=-10.0 ; x <= 10.0 ; x += 2.0 )
	{
		for ( y=-10.0 ; y <= 10.0 ; y += 2.0 )
			printf("%+6.4f ", (10-sqrt(x*x+y*y))*cos( sqrt(x*x+y*y) ) );
		printf("\n");
	}
}
