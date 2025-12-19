{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/26411cop/19-coding68/blob/main/mid-19-copter.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Wf5KrEb6vrkR"
      },
      "source": [
        "# ยินดีต้อนรับสู่ Colab"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "สอบกลางภาค โจทยืเรื่องวัดอุณหภูมิ"
      ],
      "metadata": {
        "id": "heyP3o8Vp9BR"
      }
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "306e97ad",
        "outputId": "b1a103ad-7562-4b6d-8baa-0ce13ec7f196"
      },
      "source": [
        "temperature_celsius = float(input(\"กรุณากรอกอุณหภูมิ (องศาเซลเซียส): \"))\n",
        "\n",
        "if temperature_celsius >= 37.5:\n",
        "    print(f\"อุณหภูมิ {temperature_celsius:.1f} องศาเซลเซียส: มีไข้\")\n",
        "else:\n",
        "    print(f\"อุณหภูมิ {temperature_celsius:.1f} องศาเซลเซียส: ปกติ\")"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "กรุณากรอกอุณหภูมิ (องศาเซลเซียส): 20\n",
            "อุณหภูมิ 20.0 องศาเซลเซียส: ปกติ\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "ยินดีต้อนรับสู่ Colab",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}