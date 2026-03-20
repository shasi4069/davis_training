{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMKG+EDn21Q+7jgTIrMv/h/",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/shasi4069/davis_training/blob/main/Python_Lab/second.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_zqq-8yzmfxQ",
        "outputId": "0c826ef7-3ee9-4215-d825-c5b62cabf537"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Positive, Even\n",
            "Negative, Odd\n",
            "Zero, Positive, Odd\n",
            "Negative, Even\n"
          ]
        }
      ],
      "source": [
        "def classify_number(num):\n",
        "    if num > 0:\n",
        "        print(\"Positive\", end=\", \")\n",
        "    elif num < 0:\n",
        "        print(\"Negative\", end=\", \")\n",
        "    else:\n",
        "        print(\"Zero\", end=\", \")\n",
        "\n",
        "    # Nested if for even/odd\n",
        "    if num != 0:\n",
        "        if num % 2 == 0:\n",
        "            print(\"Even\")\n",
        "        else:\n",
        "            print(\"Odd\")\n",
        "\n",
        "numbers = [10, -5, 0, 7, -2]\n",
        "\n",
        "for n in numbers:\n",
        "    classify_number(n)"
      ]
    }
  ]
}