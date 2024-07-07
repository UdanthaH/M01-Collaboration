{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d21f7853-c061-491b-9c43-d4eb5de025fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define the sum function in sum.py inside my_sum directory\n",
    "sum_code = \"\"\"\n",
    "def sum(numbers):\n",
    "    total = 0\n",
    "    for number in numbers:\n",
    "        total += number\n",
    "    return total\n",
    "\"\"\"\n",
    "\n",
    "# Write the sum function to sum.py\n",
    "with open('project/my_sum/sum.py', 'w') as file:\n",
    "    file.write(sum_code)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7540e06b-577e-4608-9fa0-940d0c45c01c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
