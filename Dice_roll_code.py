{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "def main():\n",
    "    print(\"\"\"Welcome to Dice Roll Code\\n\\n\\nPress \"space\" to roll the dice\\n\\n\\nPress Q to exit.\"\"\")\n",
    "    while True:\n",
    "        try:\n",
    "            key_pressed=input(\"Please enter the transaction:\")\n",
    "            if key_pressed==\"q\" or key_pressed==\"Q\":\n",
    "                print(\"Exiting the program, Bye...\")\n",
    "                break\n",
    "            elif key_pressed==\" \":\n",
    "                print(\"Your number:\",random.randint(1,6))\n",
    "            else:\n",
    "                raise ValueError \n",
    "        except ValueError:\n",
    "            print(\"Please enter a valid transaction.\")\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}