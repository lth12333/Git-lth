{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "163063d6-23c9-4511-86d3-9d6081c1a89a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "동전으로 교환하고자 하는 금액은? 4000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "500원 동전의 갯수 : 8 \n",
      "100원 동전의 갯수 : 0 \n",
      "50원 동전의 갯수 : 0 \n",
      "10원 동전의 갯수 : 0\n"
     ]
    }
   ],
   "source": [
    "def get_integer(prompt):\n",
    "    cost = int(input(prompt))\n",
    "    return cost\n",
    "\n",
    "def exchange(cost):\n",
    "    n500 = cost // 500\n",
    "    cost %= 500\n",
    "    n100 = cost // 100\n",
    "    cost %= 100\n",
    "    n50 = cost // 50\n",
    "    cost %= 50\n",
    "    n10 = cost // 10\n",
    "    print('500원 동전의 갯수 :', n500, '\\n100원 동전의 갯수 :', n100, '\\n50원 동전의 갯수 :', n50, '\\n10원 동전의 갯수 :', n10)\n",
    "\n",
    "cost = get_integer(\"동전으로 교환하고자 하는 금액은?\")\n",
    "exchange(cost)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e9fe3810-36a3-4f28-b33a-0c7420d7ab0f",
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
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
