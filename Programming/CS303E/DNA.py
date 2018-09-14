# File: DNA.py

# Description: An algorithm designed to find longest common substring given different pairs of DNA sequences

# Student Name: Stephen Rauner

# Student UT EID: STR428

# Course Name: CS 303E

# Unique Number: 50475

# Date Created: 10/14/2015

# Date Last Modified: 10/14/2015


# function to test if specified sub (of dna2) is present in strand (dna1)
def is_in (sub, strand):

	# loop searching through every sub of size len(sub) within strand
	for i in range(len(strand) - len(sub) + 1):

		# conditional testing if our sub ever occurs in strand
		if (sub == strand[i:(i + len(sub))]):
			return True

	return False
		

def main():
    # open file for reading
    in_file =  open ("./dna.txt", "r")

    # read number of pairs
    num_pairs = in_file.readline()
    num_pairs = num_pairs.strip()
    num_pairs = int (num_pairs)

    # create a 2D list which will contain lists for each respective pair
    commons = []

    # read each pair of dna strands
    for i in range (num_pairs):
        st1 = in_file.readline()
        st2 = in_file.readline()

        # remove white space from either end
        st1 = st1.strip()
        st2 = st2.strip()

        # make both strands upper case
        st1 = st1.upper()
        st2 = st2.upper()

        # order strands by size (dna1 is always larger or equal)
        if (len(st1) > len(st2)):
            dna1 = st1
            dna2 = st2
        else:
            dna1 = st2
            dna2 = st1

        # get all substrings of dna2
        wnd = len (dna2)

        # create list of biggest common elements; start with empty
        pair_common = []

    	# makes sure to run through every window size greater than one
        while (wnd > 1):
            start_idx = 0

            while ((start_idx + wnd) <= len (dna2)):
                sub_strand = dna2[start_idx: (start_idx + wnd)]

                # appends sub_strand to list of common pairs if it exists in dna1
                if (is_in (sub_strand, dna1) 

                    # checks if the sub_strand is already accounted for;
                    # if it is, it won't add it to the list again
                    and (pair_common.count(sub_strand) == 0)):
                    pair_common.append(sub_strand)

                # move starting place by 1
                start_idx += 1

            # once it finds a common element, it finishes
            # looking in that window and then stops looking
            if (len(pair_common) > 0):
                commons.append(pair_common)
                break

            # append commons list with an empty set if there are no common substrings
            if ((len(pair_common) == 0) and (wnd == 2)):
                commons.append([])

            # decrease window size
            wnd = wnd - 1

    # loop to format final response
    print("\nLongest Common Sequences\n")

    # first - load ith row of matrix commons
    for i in range (len(commons)):

        # immediately - check if there exist any common substrings
        if (len(commons[i]) == 0):
            print ("Pair {}: No Common Sequence Found\n".format(i + 1))
            continue

        # now - run through each element of the ith row
        for j in range (len(commons[i])):

            # only for the first element (j == 0) of the
            # set do we want to include "pair x" prior
            if (j == 0): 
                print ("Pair {}: {}".format(i + 1, commons[i][j]))

            # for all but the first, make 8 spaces then the new element
            else:
                print ("{:>8}{}".format("", commons[i][j]))
        print()


    # close file
    in_file.close()

main()