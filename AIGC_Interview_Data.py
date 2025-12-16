# -*- coding: utf-8 -*-
# This file contains data extracted from the 'WeThinkIn/AIGC-Interview-Book' repository.
# The original work is licensed under the GNU General Public License v3.0 (GPL-3.0).
# Therefore, this file and any derivative work must also be licensed under GPL-3.0.
#
# Source: https://github.com/WeThinkIn/AIGC-Interview-Book
# License: GPL-3.0 (See LICENSE file in the repository root)

# Data extracted from AIGC-Interview-Book/大模型基础/基础知识.md

AIGC_INTERVIEW_DATA = {
    "LLM中token指的是什么？": "在大语言模型中，Token是模型进行语言处理的基本信息单元，它可以是一个字，一个词甚至是一个短语句子。Token并不是一成不变的，在不同的上下文中，他会有不同的划分粒度。",
    "哪些因素会导致LLM中的偏见？": "偏见可能来源于训练数据的偏差、数据选择与采样方法、模型架构和训练方法、人类标注者的偏见以及模型部署和使用环境。为了减少偏见，需要多样化训练数据、进行偏见检测和消除、提高透明度和解释性，并持续监控和改进。",
    "如何减轻LLM中的“幻觉”现象？": "减轻幻觉现象可以通过改进训练数据质量和训练方法（如数据清洗、监督学习和强化学习）、采用后处理技术（如事实验证和编辑校对）、改进模型架构（结合外部知识库和多任务学习）、提高模型透明度和可解释性，以及建立用户教育和反馈机制。",
    "解释一下大模型的涌现能力？": "大模型的涌现能力指的是，当模型的规模和复杂度达到一定程度时，出现了一些在较小模型中未曾观察到的新特性或能力，如语言理解与生成、推理、多语言处理和少样本学习等。这些能力并非通过直接编程实现，而是在大量数据和复杂训练过程中自然涌现的。",
    "解释一下MOE，它的作用主要是什么？": "混合专家模型（Mixture of Experts：MoE）是一种稀疏门控制的深度学习模型，主要由一组专家模型和一个门控模型组成。它将输入数据根据任务类型分割成多个区域，并将每个区域的数据分配给一个或多个专家模型，从而提高模型的整体性能。",
    "如何缓解大语言模型inference时候重复的问题？": "缓解重复问题的方法包括引入重复惩罚机制、多样性采样技术（如温度采样、Top-k采样、Top-p采样）、N-gram去重、改进模型架构和训练方法（如长程记忆机制、训练数据去重）以及生成后的后处理技术。",
    "什么是大模型智能体？": "智能体是具有自主性、反应性、积极性和社交能力特征的智能实体，由三个部分组成：控制端（Brain，主要由LLMs组成）、感知端（Perception）和行动端（Action）。",
    "LLM有哪些类型？": "LLM大模型根据应用领域的不同，分为文本、音频和语音、图像和视频、以及多模态等类型。",
    "什么是基础模型？什么是开源模型，和闭源模型？": "基础模型（Foundation model）通常使用无监督或自监督学习，模型规模很大（数十亿参数），作为基座模型，仅需微调即可转变为特定应用模型。开源模型对公众开放，允许修改和定制（如LLaMA）；闭源模型为公司专有，仅对公众开放接口（如GPT-4o）。",
    "什么是语言模型？": "语言模型是一种概率模型，用于预测词元（token）序列的概率分布。它通过比较不同词元序列的联合概率，确定哪个序列在给定上下文中是最可能的，并具备语法理解和世界知识。",
    "什么是自回归语言模型？": "自回归语言模型是一种使用先前的文字来预测下一个文字的模型。它通过逐词地生成文本，每一步都基于之前生成的内容，并通过逐步预测每个位置的单词来生成一句话或一段话。",
    "什么是信息理论？": "信息理论是研究信息的度量、传递、存储和处理的学科，由克劳德·香农创立。其中最重要的概念是信息量（信息熵），用于度量信息不确定性。",
    "什么是n-gram模型？": "n-gram模型是一种用于自然语言处理和概率语言建模的基本方法。它通过统计文本中n个连续单词出现的频率来预测下一个单词的概率。在一个n-gram模型中，关于$x_{i}$的预测只依赖于最后的 $𝑛−1$ 个字符$ 𝑥_{𝑖−(𝑛−1):𝑖−1}$ 。",
    # 更多数据可以根据需要添加...
}

def get_aigc_interview_answer(question):
    """
    根据问题从AIGC面试数据中查找答案。
    """
    # 简单的关键词匹配
    for q, a in AIGC_INTERVIEW_DATA.items():
        if question.lower() in q.lower():
            return a
    return None

if __name__ == '__main__':
    print("--- AIGC_Interview_Data.py Test Mode ---")
    test_question = "什么是大模型智能体？"
    answer = get_aigc_interview_answer(test_question)
    print(f"Question: {test_question}")
    print(f"Answer: {answer}")
    
    test_question_2 = "token"
    answer_2 = get_aigc_interview_answer(test_question_2)
    print(f"\nQuestion: {test_question_2}")
    print(f"Answer: {answer_2}")
