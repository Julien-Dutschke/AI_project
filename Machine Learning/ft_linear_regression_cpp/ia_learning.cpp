#include <iostream>
#include <vector>
#include <string>
#include "rapidcsv.h"
#include "ListNormalise.hpp"

struct DataInput
{
	std::vector<float> km;
	std::vector<float> price;
};

struct DataNormalised
{
	std::vector<double> km;
	std::vector<double> price;
};


int main(int argc, char **argv)
{
	DataInput data;
	DataNormalised data_normalised;
	if (argc != 2)
	{
		std::cout << "Usage: ./ia_learning <file.csv>" << std::endl;
		return 1;
	}

	
	try
	{
		rapidcsv::Document doc(argv[1]);
		data.km = doc.GetColumn<float>("km");
		data.price = doc.GetColumn<float>("price");
		//? verify if the data is correct
		if (data.km.size() != data.price.size())
		{
			std::cerr << "Error: km and price data size are not the same" << std::endl;
			return 1;
		}
	}
	catch (const std::exception &e)
	{
		std::cerr << "Error: " << e.what() << std::endl;
		return 1;
	}

	//?--------------- Normalise the data---------------------------------?
	VectorNormalizer<float> kmNormalised(data.km);
	VectorNormalizer<float> priceNormalised(data.price);
	data_normalised.km = kmNormalised.getNormalizedVector();
	data_normalised.price = priceNormalised.getNormalizedVector();
    //?-----------------------------------------------------------------?

	// ! print the normalised data
	std::cout << "km normalised:" << std::endl;
	kmNormalised.printNormalizedVector();
	std::cout << "price normalised:" << std::endl;
	priceNormalised.printNormalizedVector();
	return 0;
}