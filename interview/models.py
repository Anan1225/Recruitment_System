from django.db import models

# Create your models here.

# 第一轮面试结果
FIRST_INTERVIEW_RESULT_TYPE = ((u'建议复试', u'建议复试'), (u'待定', u'待定'), (u'放弃', u'放弃'))
# 复试面试建议
INTERVIEW_RESULT_TYPE = ((u'建议复试', u'建议复试'), (u'待定', u'待定'), (u'放弃', u'放弃'))
# 候选人学历
DEGREE_TYPE = ((u'本科', u'本科'), (u'硕士', u'硕士'), (u'博士', u'博士'))
# HR终面结论
HR_SCORE_TYPE = (('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'))

class Candidate(models.Model):
    # 基础信息
    userid = models.IntegerField(unique=True, blank=True, null=True, verbose_name=u'ID')
    username = models.CharField(max_length=135, verbose_name=u'Name')
    city = models.CharField(max_length=135, verbose_name=u'City')
    telephone = models.CharField(max_length=135, verbose_name=u'Telephone')
    email = models.EmailField(max_length=135, blank=True, verbose_name=u'Email')
    apply_position = models.CharField(max_length=135, blank=True, verbose_name=u'Apply Position')
    born_address = models.CharField(max_length=135, blank=True, verbose_name=u'Born Address')
    gender = models.CharField(max_length=135, blank=True, verbose_name=u'Gender')
    candidate_remark = models.CharField(max_length=135, blank=True, verbose_name=u'Candidate Remark')

    # 学校与学历信息
    bachelor_school = models.CharField(max_length=135, blank=True, verbose_name=u'Bachelor School')
    master_school = models.CharField(max_length=135, blank=True, verbose_name=u'Master School')
    doctor_school = models.CharField(max_length=135, blank=True, verbose_name=u'Doctor School')
    major = models.CharField(max_length=135, blank=True, verbose_name=u'Major')
    degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name=u'Degree')

    # 综合能力测评成绩，笔试测评成绩
    test_score_of_general_ability = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True,
                                                        verbose_name=u'General Ability Score')
    paper_score = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True,
                                      verbose_name=u'Paper Score')

    # 第一轮面试记录
    first_score = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True,
                                      verbose_name=u'First Score')
    first_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                 verbose_name=u'Learning Ability Score')
    first_profession_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                      verbose_name=u'Profession Competency Score')
    first_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'Advantage')
    first_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'Disadvantage')
    first_result = models.CharField(max_length=256, choices=FIRST_INTERVIEW_RESULT_TYPE, blank=True,
                                    verbose_name=u'First Interview Result')
    first_recommend_position = models.CharField(max_length=256, blank=True, verbose_name=u'Recommend Position')
    first_interviewer = models.CharField(max_length=256, blank=True, verbose_name=u'Interviewer')
    first_remark = models.CharField(max_length=135, blank=True, verbose_name=u'First Interview Remark')

    # 第二轮面试结果
    second_score = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True, verbose_name=u'Second Score')
    second_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True, verbose_name=u'Learning Ability Score')
    second_profession_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True, verbose_name=u'Profession Competency Score')
    second_pursue_of_excellence = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True, verbose_name=u'Excellence Pur Score')
    second_communication_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True, verbose_name=u'Communication Ability Score')
    second_pressure_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True, verbose_name=u'Pressure Score')
    second_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'Advantage')
    second_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'Disadvantage')
    second_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True, verbose_name=u'Second Interview Result')
    second_recommend_position = models.CharField(max_length=256, blank=True, verbose_name=u'Recommend Position')
    second_interviewer = models.CharField(max_length=256, blank=True, verbose_name=u'Interviewer')
    second_remark = models.CharField(max_length=135, blank=True, verbose_name=u'Second Interview Remark')

    # HR终面
    HR_score = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True, verbose_name=u'HR Score')
    HR_responsibility = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u'HR Responsibility')
    HR_communication_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u'HR Communication Ability Score')
    HR_logic_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u'HR Logic Ability Score')
    HR_potential = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u'HR Potential Score')
    HR_stability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u'HR Stability Score')
    HR_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'Advantage')
    HR_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'Disadvantage')
    HR_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True, verbose_name=u'HR Interview Result')
    HR_interviewer = models.CharField(max_length=256, blank=True, verbose_name=u'HR Interviewer')
    HR_remark = models.CharField(max_length=256, blank=True, verbose_name=u'HR Interview Remark')

    # 数据记录
    creator = models.CharField(max_length=256, blank=True, verbose_name="Creator")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=u'Created Date')
    modifed_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=u'Update Date')
    last_editor = models.CharField(max_length=256, blank=True, verbose_name="Last Editor")

    class Meta:
        db_table = u'candidate'
        verbose_name = u'应聘者'
        verbose_name_plural = u'应聘者'

    def __str__(self):
        return self.username
















