{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "CcQnaVToJoMC"
   },
   "source": [
    "作業目標<br>\n",
    "熟悉陣列維度轉換，並且會擷取需要資料<br>\n",
    "作業重點<br>\n",
    "使用reshap須注意order用法<br>\n",
    "where可以運用邏輯條件擷取資料"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "JKtCM_7rJqUp"
   },
   "source": [
    "題目:<br>\n",
    "1.將下列陣列(array1)，轉成維度為(5X6)的array，順序按列填充。(hint:order=\"F\")<br>\n",
    "2.呈上題的array，找出被6除餘1的數的索引<br>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "id": "9U3itXkFKqV4"
   },
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "id": "kLjyVid_JpIC"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0,  5, 10, 15, 20, 25],\n",
       "       [ 1,  6, 11, 16, 21, 26],\n",
       "       [ 2,  7, 12, 17, 22, 27],\n",
       "       [ 3,  8, 13, 18, 23, 28],\n",
       "       [ 4,  9, 14, 19, 24, 29]])"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#1.將下列清單(list1)，轉成維度為(5X6)的array，順序按列填充。(hint:order=\"F\")\n",
    "array1 = np.array(range(30))\n",
    "array1 = array1.reshape(5,6,order=\"F\")\n",
    "array1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "id": "X1PZ16iqXWOe"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([0, 1, 2, 3, 4]), array([5, 0, 1, 2, 3]))"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#2.呈上題的array，找出被6除餘1的數的索引\n",
    "np.where(array1%6==1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "XvRQhJxNxRPd"
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "collapsed_sections": [],
   "name": "作業_題目Hong.ipynb",
   "provenance": []
  },
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
