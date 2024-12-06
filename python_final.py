{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TQggtlLF-huA"
      },
      "source": [
        "#  2024-2학기 파이썬 프로그래밍 기말고사\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OtG7xx1d_S9S"
      },
      "source": [
        "기말 고사 유의 사항\n",
        "\n",
        "1. 문제의 답안을 함수로 작성하되, 반드시 함수 이름은 문제에서 제시하는 함수명으로 할것 (함수명이 다르면 점수 획득 불가능)\n",
        "1. 각 문제의 답안은 답안 작성 셀에서 작성할 것\n",
        "1. 모든 문제는 함수의 매개변수 입력을 통해 데이터를 전달 받고, 결과를 반환하는 함수를 정의하는 것임 (주의: input()는 키보드 입력이며, 함수 입력이 아님, print()는 모니터에 출력하는 함수이며, 함수 반환이 아님)\n",
        "1. 함수의 입력과 반환 시 데이터 타입도 반드시 지킬것 (예: 문자열 반환이라는 문제에서는 반드시 문자열을 반환 해야함)\n",
        "1. 답안 제출은 함수가 정의된 부분만 제출하고, 나머지 코드는 지우고 제출할 것, 답안 제출시 input() 함수나 , print() 함수가 있으면 안됨\n",
        "1. 코드 작성이 끝난 파일은 개별적으로 함수를 호출해서 검수를 거쳐 정답이 맞는지 확인할 것\n",
        "1. 작성된 답안은 colab의 상단 메뉴의 파일--> 다운로드 --> .py 로 다운 받아 학교 LMS 에 제출할 것  ( .py 다운로드시 경고창이 뜨지만, 계속 버튼을 눌러 다운 할것)\n",
        "1. .py 가 학교 LMS 에 올라가지 않을경우 ZIP으로 압축하여 업로드 가능\n",
        "1. 파일의 이름은 자신의 학번.py      예) 학번이 2021111000 일 경우,     2021111000.py 파일을 제출\n",
        "1. 코드는 자동 채점이 되며, 각 문제당 부분 점수는 없음\n",
        "1. 시험 문제 및 답안을 절대 유출 금지(SNS, 커뮤니티 및 개인 블로그 포함)하며, 유출될 경우 불이익을 감수할 것\n",
        "1. 제출 기한을 넘겨 답안을 제출하는 것은 불가"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "G8s27iEOeMOd"
      },
      "source": [
        "## 문제 1) - 5점"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lhpvyiXLeu-1"
      },
      "source": [
        "\n",
        "<strong>* 5개의 학습활동의 점수 입력하여, 학습활동의 평균값에 대해 다음과 같은 학점을 부여한다. 5개의 정수를 입력하여 학점을 반환하는 함수를 작성하시오. </strong>\n",
        "(단, 각 학습활동의 입력값은 0에서 100까지의 정수만 입력가능하며, 이외 입력값이 들어오면 예외처리를 한다.)\n",
        "\n",
        "|5개의 학습활동 점수 평균|학점(대문자)|\n",
        "|---|---|\n",
        "|90점이상 100점이하|A|\n",
        "|80점 이상 90점 미만|B|\n",
        "|70점 이상 80점 미만|C|\n",
        "|60점 이상 70점 미만|D|\n",
        "|60점 미만|F|   \n",
        "\n",
        "<br>\n",
        "\n",
        "> 예외처리 문자열 - Invalid Value\n",
        "\n",
        "\n",
        "\n",
        "* 예1)\n",
        "  - 입력(정수, 정수, 정수, 정수) : 90, 87, 97, 89, 91 <br>\n",
        "  - 반환(문자열) : A\n",
        "\n",
        "  - 함수 입력\n",
        "    ```\n",
        "    exam1(90, 87, 97, 89, 91)\n",
        "\n",
        "    ```\n",
        "  - 함수 반환\n",
        "    ```\n",
        "    A\n",
        "\n",
        "    ```\n",
        "\n",
        "\n",
        "\n",
        "* 예2)\n",
        "  * 입력(정수, 정수, 정수, 정수) : 70, 78, 90, 21, 62 <br>\n",
        "  * 반환(문자열) : D\n",
        "\n",
        "  * 함수 입력\n",
        "    ```\n",
        "    exam1(70, 78, 90, 21, 62)\n",
        "\n",
        "    ```\n",
        "  * 함수 반환\n",
        "    ```\n",
        "    D\n",
        "\n",
        "    ```\n",
        "\n",
        "* 예3)\n",
        "  * 입력(정수, 정수, 정수, 정수) : 120, 1001, 202, 80, 11 <br>\n",
        "  * 반환(문자열) : Invalid Value\n",
        "\n",
        "  * 함수 입력\n",
        "    ```\n",
        "    exam1(120, 1001, 202, 80, 11)\n",
        "\n",
        "    ```\n",
        "  * 함수 반환\n",
        "    ```\n",
        "    Invalid Value\n",
        "\n",
        "    ```\n",
        "\n",
        "\n",
        "\n",
        "* 함수 이름: exam1<br>      (반드시 함수 이름을 exam1로 작성할것!!)\n",
        "\n",
        "* 함수 작성 가이드 <br>\n",
        "\n",
        "\n",
        "\n",
        "```\n",
        "def exam1(a, b, c, d, e):\n",
        "    grade = a, b, c, d, e 의 평균에 대한 학점\n",
        "    return grade\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "cb4AtnIZIGyA"
      },
      "outputs": [],
      "source": [
        "###### 1번 문제 답안 작성 셀 ######\n",
        "\n",
        "def exam1(a, b, c, d, e):\n",
        "    # 입력값 범위 확인\n",
        "    scores = [a, b, c, d, e]\n",
        "    if not all(0 <= score <= 100 for score in scores):\n",
        "        return \"Invalid Value\"\n",
        "\n",
        "    # 평균 계산\n",
        "    avg = sum(scores) / len(scores)\n",
        "\n",
        "    # 학점 부여\n",
        "    if avg >= 90:\n",
        "        return \"A\"\n",
        "    elif avg >= 80:\n",
        "        return \"B\"\n",
        "    elif avg >= 70:\n",
        "        return \"C\"\n",
        "    elif avg >= 60:\n",
        "        return \"D\"\n",
        "    else:\n",
        "        return \"F\""
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "X1GukuNA-vPR"
      },
      "source": [
        "## 문제 2) - 13점"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kK4fr_Gm5oCl"
      },
      "source": [
        "<strong> * 하나의 리스트를 함수의 입력으로 넣으면, 리스트안의 중복을 제거한 다음 중복 제거된 리스트를 반환하는 함수를 작성하시오. (단, 리스트 내 데이터 순서를 유지할 것)</strong>\n",
        "\n",
        "* 예1)\n",
        "   * 입력(리스트) : [1,2,1,1,2,4] <br>\n",
        "   * 반환(리스트) : [1,2,4]\n",
        "\n",
        "   * 함수 입력\n",
        "       ```\n",
        "       exam2([1,2,1,1,2,4])\n",
        "\n",
        "       ```\n",
        "   * 함수 반환\n",
        "       ```\n",
        "       [1,2,4]\n",
        "\n",
        "       ```\n",
        "\n",
        "* 예2)\n",
        "\n",
        "  * 입력(리스트): [3,3,4,5,3] <br>\n",
        "  * 반환(리스트): [3,4,5]\n",
        "\n",
        "  * 함수 입력\n",
        "    ```\n",
        "    exam2([3,3,4,5,3])\n",
        "\n",
        "    ```\n",
        "  * 함수 반환\n",
        "    ```\n",
        "    [3,4,5]\n",
        "\n",
        "    ```\n",
        "\n",
        "\n",
        "\n",
        "* 함수 이름: exam2 <br>      (반드시 함수 이름을 exam2로 작성할것!!)\n",
        "\n",
        "* 함수 작성 가이드 <br>\n",
        "\n",
        "\n",
        "\n",
        "```\n",
        "def exam2(a):\n",
        "    b = a리스트의 중복제거한 리스트\n",
        "    return b\n",
        "```\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "kX9xY63-5j5p"
      },
      "outputs": [],
      "source": [
        "###### 2번 문제 답안 작성 셀 ######\n",
        "\n",
        "\n",
        "def exam2(a):\n",
        "    result = []\n",
        "    for item in a:\n",
        "        if item not in result:\n",
        "            result.append(item)\n",
        "    return result"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EnqoaId9BzIm"
      },
      "source": [
        "## 문제 3) - 7점"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "smtRGTyPBqxk"
      },
      "source": [
        "<strong> 다음 표에서 나타내는 아이스크림 중, 2가지를 선택하여 함수의 입력으로 아이스크림의 이름과 수량 정보가 리스트를 입력하면 아이스크림의 총 가격이 반환하는 함수를 작성하시오.</strong> (단, 아이스크림의 순서는 상관없음)\n",
        "\n",
        "|아이스크림|가격|\n",
        "|---|---|\n",
        "|누가바|500|\n",
        "|돼지바|600|\n",
        "|바밤바|900|\n",
        "|보석바|300|\n",
        "|메로나|400|\n",
        "|쌍쌍바|700|\n",
        "\n",
        "* 예1)\n",
        "\n",
        "  * 입력(딕셔너리를 요솟값으로 하는 리스트) : [{\"누가바\": 1}, {\"쌍쌍바\": 2}]\n",
        "  * 반환(정수) : 1900\n",
        "\n",
        "  * 함수 입력\n",
        "    ```   \n",
        "    exam3([{\"누가바\": 1}, {\"쌍쌍바\": 2}])\n",
        "    ```\n",
        "  * 함수 반환\n",
        "    ```\n",
        "    1900\n",
        "    ```\n",
        "\n",
        "* 예2)\n",
        "\n",
        "  * 입력(딕셔너리를 요솟값으로 하는 리스트): [{\"돼지바\": 2}, {\"바밤바\": 1}]\n",
        "  * 반환(정수): 2100\n",
        "\n",
        "\n",
        "  * 함수 입력\n",
        "    ```\n",
        "    exam3([{\"돼지바\": 2}, {\"바밤바\": 1}])\n",
        "    ```\n",
        "\n",
        "  * 함수 반환\n",
        "    ```\n",
        "    2100\n",
        "    ```\n",
        "\n",
        "* 함수 이름: exam3\n",
        "(반드시 함수 이름을 exam3로 작성할것!!)\n",
        "\n",
        "* 함수 작성 가이드\n",
        "\n",
        "\n",
        "\n",
        "```\n",
        "def exam3(a):\n",
        "    e = a 리스트에서 나타낸 아이스크림의 가격 합계\n",
        "    return e\n",
        "```\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "id": "FS8nRvcNG8QR"
      },
      "outputs": [],
      "source": [
        "###### 3번 문제 답안 작성 셀 ######\n",
        "\n",
        "def exam3(a):\n",
        "    prices = {\n",
        "        \"누가바\": 500,\n",
        "        \"돼지바\": 600,\n",
        "        \"바밤바\": 900,\n",
        "        \"보석바\": 300,\n",
        "        \"메로나\": 400,\n",
        "        \"쌍쌍바\": 700\n",
        "    }\n",
        "\n",
        "    total = 0\n",
        "    for item in a:\n",
        "        for name, quantity in item.items():\n",
        "            total += prices[name] * quantity\n",
        "    return total"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8uQNXmPWHHGN"
      },
      "source": [
        "## 문제 4) - 10점"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PLsesGlrHyvc"
      },
      "source": [
        "<strong> 영어단어와 그 뒤에 1부터 9까지의 정수가 합쳐진 문자열이 합수의 입력으로 들어오면 숫자를 영문자열로 변환하여 반환하는 함수를 작성하시오.  </strong>\n",
        "(단, 모든 반환 문자열은 소문자이다.)\n",
        "\n",
        "\n",
        "\n",
        "* 예1)<br>\n",
        "\n",
        "    * 입력(문자열) : apple1<br>\n",
        "    * 반환(문자열) : appleone<br>\n",
        "\n",
        "    * 함수 입력\n",
        "        ```\n",
        "        exam4(\"apple1\")\n",
        "\n",
        "        ```\n",
        "\n",
        "    * 함수 반환\n",
        "\n",
        "        ```\n",
        "        appleone\n",
        "\n",
        "        ```\n",
        "\n",
        "* 예3)<br>\n",
        "\n",
        "    * 입력(문자열) : banana7<br>\n",
        "    * 반환(문자열) : bananaseven<br>\n",
        "\n",
        "    * 함수 입력\n",
        "        ```\n",
        "        exam4(\"banana7\")\n",
        "\n",
        "        ```\n",
        "    \n",
        "    * 함수 반환\n",
        "        ```\n",
        "        bananaseven\n",
        "        ```\n",
        "\n",
        "* 예2)<br>\n",
        "\n",
        "    * 입력(문자열) : melon9<br>\n",
        "    * 반환(문자열) : melonnine<br>\n",
        "\n",
        "    * 함수 입력\n",
        "        ```\n",
        "        exam4(\"melon9\")\n",
        "\n",
        "        ```\n",
        "    \n",
        "    * 함수 반환\n",
        "        ```\n",
        "        melonnine\n",
        "        ```\n",
        "\n",
        "\n",
        "* 함수 이름: exam4  <br>\n",
        "(반드시 함수 이름을 exam4로 작성할것!!)<br>\n",
        "\n",
        "* 함수 작성 가이드\n",
        "\n",
        "```\n",
        "def exam4(a):\n",
        "    b = a의 숫자를 영문자열로 반환한 문자열\n",
        "    return b\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "id": "71qGTeWEW14L"
      },
      "outputs": [],
      "source": [
        "###### 4번 문제 답안 작성 셀 ######\n",
        "\n",
        "def exam4(a):\n",
        "    number_words = {\n",
        "        '1': 'one',\n",
        "        '2': 'two',\n",
        "        '3': 'three',\n",
        "        '4': 'four',\n",
        "        '5': 'five',\n",
        "        '6': 'six',\n",
        "        '7': 'seven',\n",
        "        '8': 'eight',\n",
        "        '9': 'nine'\n",
        "    }\n",
        "\n",
        "    word = a[:-1]\n",
        "    number = a[-1]\n",
        "    return word + number_words[number]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ApVnFiekZWbv"
      },
      "source": [
        "## 문제5) - 5점"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "AOx7f5T9ZzH8"
      },
      "source": [
        "<strong> 2004년도부터 2100년도까지의 정수를 함수의 입력으로 넣으면, 올림픽 개최의 해인지 판별하여 개최의 해라면 True, 그렇지 않다면 False를 반환하는 함수를 작성하시오.  </strong><br>\n",
        "\n",
        "(단, 2004년도는 올림픽 개최의 해 이며, 4년마다 한번씩 올림픽이 개최되어 이후 2008, 2012..... 년도 등이 올림픽이 개최의 해이다.)\n",
        "\n",
        "\n",
        "\n",
        "* 예1)<br>\n",
        "\n",
        "  * 입력(정수) : 2004<br>\n",
        "  * 반환(bool) : True<br>\n",
        "\n",
        "  * 함수 입력\n",
        "      ```\n",
        "      exam5(2004)\n",
        "    \n",
        "      ```\n",
        "  * 함수 반환\n",
        "    \n",
        "     ```\n",
        "    True\n",
        "     ```\n",
        "<br>\n",
        "\n",
        "* 예2)\n",
        "\n",
        "  * 입력(정수) : 2003<br>\n",
        "  * 반환(bool) : False<br>\n",
        "  * 함수 입력\n",
        "      ```\n",
        "      exam5(2003)\n",
        "\n",
        "      ```\n",
        "\n",
        "  * 함수 반환\n",
        "\n",
        "      ```\n",
        "      False\n",
        "      ```\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "* 함수 이름: exam5\n",
        "(반드시 함수 이름을 exam5로 작성할것!!)\n",
        "\n",
        "* 함수 작성 가이드\n",
        "\n",
        "\n",
        "```\n",
        "\n",
        "def exam5(a):\n",
        "    b = a 가 올림픽 개최의 해라면 True(bool). 그렇지 않다면 False(bool)을 대입\n",
        "    return b\n",
        "```\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "id": "N1DpVBJmIs_L"
      },
      "outputs": [],
      "source": [
        "###### 5번 문제 답안 작성 셀 ######\n",
        "\n",
        "\n",
        "def exam5(a):\n",
        "    if a < 2004:\n",
        "        return False\n",
        "    return (a - 2004) % 4 == 0 and a <= 2100\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "R9k6o23RMER4"
      },
      "source": [
        "## 문제 6) - 5점"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IQWD9SCNhgHP"
      },
      "source": [
        "<strong>전화번호를 함수의 입력으로 넣으면, 해당 전화번호의 지역을 반환하는 함수를 작성하시오.</strong><br>\n",
        "\n",
        "단, 아래의 지역번호로된 전화번호만 함수의 입력으로 주어진다고 가정한다.\n",
        "\n",
        "\n",
        "|지역번호 |지역|\n",
        "|---|---|\n",
        "|02|서울|\n",
        "|031|경기|\n",
        "|033|강원|\n",
        "|044|대전|\n",
        "\n",
        "\n",
        "\n",
        "* 예1)<br>\n",
        "\n",
        "  * 입력(문자열) : 02-2244-7778<br>\n",
        "  * 반환(문자열) : 서울<br>\n",
        "\n",
        "  * 함수 입력\n",
        "      ```\n",
        "      exam6(\"02-2244-7778\")\n",
        "    \n",
        "      ```\n",
        "  * 함수 반환\n",
        "    \n",
        "     ```\n",
        "     서울\n",
        "     ```\n",
        "\n",
        "* 예2)\n",
        "\n",
        "    * 입력(문자열) : 033-5547-8874<br>\n",
        "    * 반환(문자열) : 강원<br>\n",
        "\n",
        "    * 함수 입력\n",
        "        ```\n",
        "        exam6(\"033-5547-8874\")\n",
        "        \n",
        "        ```\n",
        "    * 함수 반환\n",
        "        \n",
        "        ```\n",
        "        강원\n",
        "        ```\n",
        "\n",
        "\n",
        "* 함수 이름: exam6\n",
        "(반드시 함수 이름을 exam6로 작성할것!!)\n",
        "\n",
        "* 함수 작성 힌트\n",
        "\n",
        "\n",
        "```\n",
        "\n",
        "def exam6(a):\n",
        "    b = a 전화번호의 지역\n",
        "    return b\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "id": "BUjtiJV_iikS"
      },
      "outputs": [],
      "source": [
        "###### 6번 문제 답안 작성 셀 ######\n",
        "\n",
        "\n",
        "def exam6(a):\n",
        "    area_codes = {\n",
        "        \"02\": \"서울\",\n",
        "        \"031\": \"경기\",\n",
        "        \"033\": \"강원\",\n",
        "        \"044\": \"대전\"\n",
        "    }\n",
        "\n",
        "    code = a.split(\"-\")[0]\n",
        "    return area_codes[code]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4-41iqJ5W1r1"
      },
      "source": [
        "## 문제 7) - 15점"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kqoNGOnfXd1T"
      },
      "source": [
        "\n",
        "<strong> 하나의 문자열을 함수의 입력으로 받으면 다음과 같은 규칙을 적용하여 문자열을 변환하여 반환하는 함수를 작성하시오. </strong><br>\n",
        "\n",
        "- 문자열의 각 단어를 반대로 뒤집는다.\n",
        "- 뒤집힌 단어들 중 단어 길이가 짝수인 것은 대문자로 변환한다.\n",
        "- 기존 문자열에서 각 단어는 원래의 순서를 유지한다.\n",
        "\n",
        "\n",
        "* 예1)<br>\n",
        "\n",
        "  * 입력(문자열) : \"hello world python\"<br>\n",
        "  * 반환(문자열) : \"olleh dlrow NOHTYP\"<br>\n",
        "  \n",
        "  * 함수 입력\n",
        "      ```\n",
        "      exam7(\"hello world python\")\n",
        "    \n",
        "      ```\n",
        "  * 함수 반환\n",
        "    \n",
        "     ```\n",
        "     olleh dlrow NOHTYP\n",
        "     ```\n",
        "\n",
        "* 예2)<br>\n",
        "\n",
        "    * 입력(문자열) : \"this is a test\"<br>\n",
        "    * 반환(문자열) : \"SIHT SI a TSET\"<br>\n",
        "\n",
        "    * 함수 입력\n",
        "        ```\n",
        "        exam7(\"this is a test\")\n",
        "        \n",
        "        ```\n",
        "    * 함수 반환\n",
        "        \n",
        "        ```\n",
        "        SIHT SI a TSET\n",
        "        ```\n",
        "\n",
        "* 함수 이름: exam7\n",
        "(반드시 함수 이름을 exam7로 작성할것!!)\n",
        "\n",
        "* 함수 작성 가이드\n",
        "\n",
        "\n",
        "```\n",
        "\n",
        "def exam7(a):\n",
        "    b = a 문자열의 각 단어를 반대로 뒤집고, 단어가 짝수이면 대문자로 변환\n",
        "    return b\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "id": "4pdCE84Fe9Ce"
      },
      "outputs": [],
      "source": [
        "###### 7번 문제 답안 작성 셀 ######\n",
        "\n",
        "def exam7(a):\n",
        "    words = a.split()\n",
        "    result = []\n",
        "\n",
        "    for word in words:\n",
        "        reversed_word = word[::-1]\n",
        "        if len(word) % 2 == 0:\n",
        "            reversed_word = reversed_word.upper()\n",
        "        result.append(reversed_word)\n",
        "\n",
        "    return \" \".join(result)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6gmPtFuZeqIj"
      },
      "source": [
        "## 문제 8 - 10점"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "mNSyCPn-fGBy"
      },
      "source": [
        "<strong>정수로 구성된 중첩된 리스트를 입력으로 받으면, 중첩된 리스트 안의 모든 정수들 중 가장 큰 값을 반환하는 함수를 작성하시오. </strong><br>\n",
        "\n",
        "\n",
        "* 예1)<br>\n",
        "\n",
        "  * 입력(리스트) : [[3, 1, 4], [1, 5, 9], [2, 6, 5, 3], [5]]<br>\n",
        "  * 반환(정수) : 9<br>\n",
        "\n",
        "  * 함수 입력\n",
        "      ```\n",
        "      exam8([[3, 1, 4], [1, 5, 9], [2, 6, 5, 3], [5]])\n",
        "    \n",
        "      ```\n",
        "  * 함수 반환\n",
        "    \n",
        "     ```\n",
        "     9\n",
        "     ```\n",
        "\n",
        "* 예2)<br>\n",
        "\n",
        "    * 입력(리스트) : [[10, 20], [-7, 40], [50]]<br>\n",
        "    * 반환(정수) : 50 <br>\n",
        "\n",
        "    * 함수 입력\n",
        "        ```\n",
        "        exam8([[10, 20], [-7, 40], [50]])\n",
        "        \n",
        "        ```\n",
        "    * 함수 반환\n",
        "        \n",
        "        ```\n",
        "        50\n",
        "        ```\n",
        "\n",
        "* 함수 이름: exam8\n",
        "(반드시 함수 이름을 exam8로 작성할것!!)\n",
        "\n",
        "* 함수 작성 가이드\n",
        "\n",
        "\n",
        "```\n",
        "\n",
        "def exam8(a):\n",
        "    b = a의 리스트 중 가장 큰 정수\n",
        "    return b\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "id": "tFpu6fEehCG6"
      },
      "outputs": [],
      "source": [
        "###### 8번 문제 답안 작성 셀 ######\n",
        "\n",
        "\n",
        "def exam8(a):\n",
        "    max_num = float('-inf')\n",
        "    for sublist in a:\n",
        "        current_max = max(sublist)\n",
        "        if current_max > max_num:\n",
        "            max_num = current_max\n",
        "    return max_num"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_6nwI88OhsBI"
      },
      "source": [
        "## 문제 9) - 15점"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "pxTuZRhohj7h"
      },
      "source": [
        "하나의 문자열을 함수의 입력으로 받으면, 다음 조건에 따라 결과를 반환하는 함수를 작성하시오.\n",
        "\n",
        "- 문자열에서 가장 많이 등장하는 문자와 두 번째로 많이 등장하는 문자를 찾아 그 문자와 등장횟수를 딕셔너리로 만든다.\n",
        "- 두 개의 딕셔너리를 담은 리스트를 함수로 반환한다.\n",
        "- 단 문자열의 등장횟수가 서로 같을 때는, 먼저 등장한 문자를 우선하여 반환한다.\n",
        "- 입력되는 모든 문자열은 소문자로 가정한다.\n",
        "\n",
        "\n",
        "\n",
        "* 예1) <br>\n",
        "\n",
        "    * 입력(문자열) : \"mississippi\"<br>\n",
        "    * 반환(리스트) : [{'i':4},{'s', 4}]<br>\n",
        "\n",
        "\n",
        "    * 함수 입력\n",
        "       ```\n",
        "       exam9(\"mississippi\")\n",
        "       ```\n",
        "\n",
        "    * 함수 반환\n",
        "        ```\n",
        "        [{'i':4},{'s', 4}]\n",
        "        ```\n",
        "\n",
        "* 예2)<br>\n",
        "\n",
        "    * 입력(문자열) : \"arrangement\"<br>\n",
        "    * 반환(리스트) : [{'a': 2},{'r':2}]<br>\n",
        "\n",
        "    * 함수 입력\n",
        "        ```\n",
        "        exam9(\"arrangement\")\n",
        "            \n",
        "        ```\n",
        "    * 함수 반환\n",
        "         \n",
        "        ```\n",
        "        [{'a': 2},{'r':2}]\n",
        "        ```\n",
        "\n",
        "* 예3)<br>\n",
        "\n",
        "    * 입력(문자열) : \"aaabbc\"<br>\n",
        "    * 반환(리스트) : [{'a': 3},{'b':2}]<br>\n",
        "\n",
        "    * 함수 입력\n",
        "        ```\n",
        "        exam9(\"aaabbc\")\n",
        "            \n",
        "        ```\n",
        "    * 함수 반환\n",
        "         \n",
        "        ```\n",
        "        [{'a': 3},{'b':2}]\n",
        "        ```        \n",
        "\n",
        "* 함수 이름: exam9 (반드시 함수 이름을 exam9로 작성할것!!)<br>\n",
        "\n",
        "함수 작성 가이드\n",
        "\n",
        "```\n",
        "\n",
        "def exam9(a):\n",
        "    b = a 문자열에서 첫번째로 많이 등장한 문자와 두번째로 등장한 문자와 등장횟수를 딕셔너리로 저장한 리스트\n",
        "    return b\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "id": "sLhBSwBMleAX"
      },
      "outputs": [],
      "source": [
        "###### 9번 문제 답안 작성 셀 ######\n",
        "\n",
        "\n",
        "def exam9(a):\n",
        "    # 문자 빈도수 계산\n",
        "    char_count = {}\n",
        "    for char in a:\n",
        "        if char in char_count:\n",
        "            char_count[char] += 1\n",
        "        else:\n",
        "            char_count[char] = 1\n",
        "\n",
        "    # 빈도수로 정렬하고, 같은 빈도수일 경우 먼저 등장한 문자 우선\n",
        "    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], a.index(x[0])))\n",
        "\n",
        "    return [{sorted_chars[0][0]: sorted_chars[0][1]},\n",
        "            {sorted_chars[1][0]: sorted_chars[1][1]}]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "y8wpZYPsli87"
      },
      "source": [
        "## 문제 10) - 15점"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-q7Zvh2clp73"
      },
      "source": [
        "<strong> 컴플레인을 받은 사람의 이름을 적어놓은 리스트가 있다. 이 리스트를 함수의 입력으로 넣으면, 컴플레인을 가장 많이 받은 사람의 이름과 횟수를 반환하는 함수를 작성하시오. (단, 동일한 컴플레인의 횟수가 없다고 가정한다.) </strong>\n",
        "\n",
        "\n",
        "\n",
        "* 예1) <br>\n",
        "\n",
        "   * 입력(리스트) : [\"Oliver\", \"Joseph\", \"Joseph\", \"Joseph\", \"Peter\", \"Oliver\",\"Nicholas\"] <br>\n",
        "   * 반환(딕셔너리) : {\"Joseph\":3} <br>\n",
        "\n",
        "\n",
        "   * 함수 입력\n",
        "      ```\n",
        "      exam10([\"Oliver\", \"Joseph\", \"Joseph\", \"Joseph\", \"Peter\", \"Oliver\",\"Nicholas\"])\n",
        "      ```\n",
        "        \n",
        "   * 함수 반환\n",
        "      ```\n",
        "      {\"Joseph\":3}\n",
        "      ```\n",
        "\n",
        "* 예2)<br>\n",
        "\n",
        "    * 입력(리스트) : [\"Kim\", \"Kim\", \"Park\"] <br>\n",
        "    * 반환(문자열) : {\"Kim\":2} <br>\n",
        "\n",
        "    * 함수 입력\n",
        "        ```\n",
        "        exam10([\"Kim\", \"Kim\", \"Park\"])                 \n",
        "        ```\n",
        "        \n",
        "    * 함수 반환\n",
        "            \n",
        "        ```\n",
        "        {\"Kim\":2}\n",
        "        ```\n",
        "\n",
        "\n",
        "\n",
        "* 함수 이름: exam10 (반드시 함수 이름을 exam10로 작성할것!!)<br>\n",
        "\n",
        "함수 작성 가이드\n",
        "\n",
        "```\n",
        "\n",
        "def exam10(a):\n",
        "    b = a 리스트에서 등장 횟수가 가장 많은 사람의 이름과 횟수를 딕셔너리로 반환\n",
        "    return b\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "id": "yMcdEi7LlpIF"
      },
      "outputs": [],
      "source": [
        "###### 10번 문제 답안 작성 셀######\n",
        "\n",
        "def exam10(a):\n",
        "    # 컴플레인 횟수 계산\n",
        "    complaints = {}\n",
        "    for name in a:\n",
        "        if name in complaints:\n",
        "            complaints[name] += 1\n",
        "        else:\n",
        "            complaints[name] = 1\n",
        "\n",
        "    # 가장 많은 컴플레인을 받은 사람 찾기\n",
        "    max_name = max(complaints.items(), key=lambda x: x[1])\n",
        "    return {max_name[0]: max_name[1]}\n"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "python-final.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3.10.5 64-bit",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "name": "python",
      "version": "3.10.5"
    },
    "vscode": {
      "interpreter": {
        "hash": "818e61c07054e900cca3fb47f365ca8e4faed981f62945c80b398dee828b08c1"
      }
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}