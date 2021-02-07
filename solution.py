{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "### welcome_assignment_answers\n",
    "### Input - All eight questions given in the assignment.\n",
    "### Output - The right answer for the specific question.\n",
    "\n",
    "def welcome_assignment_answers(question):\n",
    "    #The student doesn't have to follow the skeleton for this assignment.\n",
    "    #Another way to implement is using a \"case\" statements similar to C.\n",
    "    if question == \"Are encoding and encryption the same? - Yes/No\":\n",
    "        answer = \"No\"\n",
    "    elif question == \"Is it possible to decrypt a message without a key? - Yes/No\":\n",
    "        answer = \"No\"\n",
    "    elif question == \"Is it possible to decode a message without a key? - Yes/No\":\n",
    "        answer = \"Yes\"\n",
    "    elif question == \"Is a hashed message supposed to be un-hashed? - Yes/No\":\n",
    "        answer = \"No\"\n",
    "    elif question == \"What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code\":\n",
    "        answer = \"42b76fe51778764973077a5a94056724\"\n",
    "    elif question == \"Is MD5 a secured hashing algorithm? - Yes/No\":\n",
    "        answer = \"No\"\n",
    "    elif question == \"What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number\":\n",
    "        answer = 1\n",
    "    elif question == \"What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number\":\n",
    "        answer = 2\n",
    "\n",
    "    return(answer)\n",
    "# Complete all the questions.\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    #use this space to debug and verify that the program works\n",
    "    debug_question = \"What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number\"\n",
    "    print(welcome_assignment_answers(debug_question))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\kaushal.mehta'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
