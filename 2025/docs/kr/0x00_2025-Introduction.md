<link rel="stylesheet" href="../../assets/css/RC-stylesheet.css" />

# 소개 (Introduction)

![OWASP Logo](../../assets/TOP_10_logo_Final_Logo_Colour.png)

OWASP Top 10의 8번째 버전에 오신 것을 환영합니다!

설문조사에 데이터와 관점을 기여해주신 모든 분들께 감사드립니다. 여러분 없이는 이번 버전이 불가능했을 것입니다. **감사합니다!**

해당 버전은 RC1버전에 대한 기계번역 버전이므로 추후 정식 버전에 대한 한국어번역 번역이 출시 될 예정입니다.

## OWASP Top 10:2025 소개 (Introducing the OWASP Top 10:2025)



* [A01:2025 - 접근 제어 취약점 (Broken Access Control)](A01_2025-Broken_Access_Control.md)
* [A02:2025 - 보안 설정 오류 (Security Misconfiguration)](A02_2025-Security_Misconfiguration.md)
* [A03:2025 - 소프트웨어 공급망 실패 (Software Supply Chain Failures)](A03_2025-Software_Supply_Chain_Failures.md)
* [A04:2025 - 암호화 실패 (Cryptographic Failures)](A04_2025-Cryptographic_Failures.md)
* [A05:2025 - 인젝션 (Injection)](A05_2025-Injection.md)
* [A06:2025 - 불안전한 설계 (Insecure Design)](A06_2025-Insecure_Design.md)
* [A07:2025 - 인증 실패 (Authentication Failures)](A07_2025-Authentication_Failures.md)
* [A08:2025 - 소프트웨어 또는 데이터 무결성 실패 (Software or Data Integrity Failures)](A08_2025-Software_or_Data_Integrity_Failures.md)
* [A09:2025 - 로깅 및 알림 실패 (Logging & Alerting Failures)](A09_2025-Logging_and_Alerting_Failures.md)
* [A10:2025 - 예외 조건 처리 오류 (Mishandling of Exceptional Conditions)](A10_2025-Mishandling_of_Exceptional_Conditions.md)


## 2025년 Top 10의 변경 사항 (What's changed in the Top 10 for 2025)

2025년 Top 10에는 두 개의 새로운 카테고리와 하나의 통합이 있습니다. 우리는 가능한 한 증상보다 근본 원인에 초점을 맞추기 위해 노력했습니다. 소프트웨어 엔지니어링과 소프트웨어 보안의 복잡성으로 인해 어느 정도의 중복 없이 10개의 카테고리를 만드는 것은 기본적으로 불가능합니다.

![Mapping](../../assets/2025-mappings.png)

* **[A01:2025 - 접근 제어 취약점 (Broken Access Control)](A01_2025-Broken_Access_Control.md)** 은 가장 심각한 애플리케이션 보안 위험으로 #1 위치를 유지합니다. 기여된 데이터에 따르면 테스트된 애플리케이션의 평균 3.73%가 이 카테고리의 40개 공통 취약점 열거(Common Weakness Enumerations, CWE) 중 하나 이상을 가지고 있었습니다. 위 그림의 점선으로 표시된 바와 같이, 서버 측 요청 위조(Server-Side Request Forgery, SSRF)가 이 카테고리에 포함되었습니다.
* **[A02:2025 - 보안 설정 오류 (Security Misconfiguration)](A02_2025-Security_Misconfiguration.md)** 는 2021년의 #5에서 2025년 #2로 상승했습니다. 이번 주기 데이터에서 설정 오류가 더 널리 퍼져 있습니다. 테스트된 애플리케이션의 3.00%가 이 카테고리의 16개 CWE 중 하나 이상을 가지고 있었습니다. 소프트웨어 엔지니어링이 설정 기반 애플리케이션 동작의 양을 계속 증가시키고 있기 때문에 이는 놀라운 일이 아닙니다.
* **[A03:2025 - 소프트웨어 공급망 실패 (Software Supply Chain Failures)](A03_2025-Software_Supply_Chain_Failures.md)** 는 [A06:2021-취약하고 오래된 구성 요소 (Vulnerable and Outdated Components)](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)를 확장하여 소프트웨어 종속성, 빌드 시스템, 배포 인프라의 전체 생태계 내에서 또는 전체에 걸쳐 발생하는 모든 공급망 손상의 더 넓은 범위를 포함합니다. 이 카테고리는 커뮤니티 설문조사에서 압도적으로 최우선 관심사로 투표되었습니다. 이 카테고리는 5개의 CWE를 가지고 있으며 수집된 데이터에서 제한적인 존재를 보이지만, 우리는 이것이 테스트의 어려움 때문이라고 믿으며 이 영역에서 테스트가 따라잡기를 희망합니다. 이 카테고리는 데이터에서 발생 빈도가 가장 낮지만, CVE에서 평균 악용 가능성 및 영향 점수가 가장 높습니다.
* **[A04:2025 - 암호화 실패 (Cryptographic Failures)](A04_2025-Cryptographic_Failures.md)** 는 순위에서 #2에서 #4로 두 단계 하락했습니다. 기여된 데이터에 따르면 평균적으로 애플리케이션의 3.80%가 이 카테고리의 32개 CWE 중 하나 이상을 가지고 있습니다. 이 카테고리는 종종 민감한 데이터 노출 또는 시스템 손상으로 이어집니다.
* **[A05:2025 - 인젝션 (Injection)](A05_2025-Injection.md)** 는 순위에서 #3에서 #5로 두 단계 하락했으며, 암호화 실패(Cryptographic Failures) 및 불안전한 설계(Insecure Design)에 비해 상대적 위치를 유지했습니다. 인젝션은 가장 많이 테스트되는 카테고리 중 하나이며, 이 카테고리의 38개 CWE와 관련된 CVE 수가 가장 많습니다. 인젝션은 크로스 사이트 스크립팅(Cross-site Scripting, 높은 빈도/낮은 영향)부터 SQL 인젝션(SQL Injection, 낮은 빈도/높은 영향) 취약점까지 다양한 문제를 포함합니다.
* **[A06:2025 - 불안전한 설계 (Insecure Design)](A06_2025-Insecure_Design.md)** 는 보안 설정 오류(Security Misconfiguration)와 소프트웨어 공급망 실패(Software Supply Chain Failures)가 이를 추월하면서 순위에서 #4에서 #6으로 두 단계 하락했습니다. 이 카테고리는 2021년에 도입되었으며, 우리는 업계에서 위협 모델링과 보안 설계에 대한 더 큰 강조와 관련된 눈에 띄는 개선을 보았습니다.
* **[A07:2025 - 인증 실패 (Authentication Failures)](A07_2025-Authentication_Failures.md)** 는 약간의 이름 변경(이전에는 "[식별 및 인증 실패 (Identification and Authentication Failures)](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/)")과 함께 #7 위치를 유지합니다. 이 카테고리의 36개 CWE를 더 정확하게 반영하기 위한 것입니다. 이 카테고리는 여전히 중요하지만, 인증을 위한 표준화된 프레임워크 사용 증가가 인증 실패 발생에 유익한 영향을 미치는 것으로 보입니다.
* **[A08:2025 - 소프트웨어 또는 데이터 무결성 실패 (Software or Data Integrity Failures)](A08_2025-Software_or_Data_Integrity_Failures.md)** 는 목록에서 #8을 계속 유지합니다. 이 카테고리는 소프트웨어 공급망 실패(Software Supply Chain Failures)보다 낮은 수준에서 소프트웨어, 코드, 데이터 아티팩트의 무결성을 검증하고 신뢰 경계를 유지하는 실패에 초점을 맞춥니다. 
* **[A09:2025 - 로깅 및 알림 실패 (Logging & Alerting Failures)](A09_2025-Logging_and_Alerting_Failures.md)** 는 #9 위치를 유지합니다. 이 카테고리는 약간의 이름 변경(이전 [보안 로깅 및 모니터링 실패 (Security Logging and Monitoring Failures)](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/))이 있어 관련 로깅 이벤트에 대한 적절한 조치를 유도하는 데 필요한 알림 기능의 중요성을 강조합니다. 훌륭한 로깅이라도 알림이 없으면 보안 사고 식별에 최소한의 가치만 있습니다. 이 카테고리는 항상 데이터에서 과소 대표될 것이며, 커뮤니티 설문조사 참가자들로부터 다시 목록의 위치로 투표되었습니다.
* **[A10:2025 - 예외 조건 처리 오류 (Mishandling of Exceptional Conditions)](A10_2025-Mishandling_of_Exceptional_Conditions.md)** 는 2025년의 새로운 카테고리입니다. 이 카테고리는 부적절한 오류 처리, 논리 오류, 실패 시 열림(failing open), 그리고 시스템이 마주칠 수 있는 비정상적인 조건에서 비롯된 기타 관련 시나리오에 초점을 맞춘 24개의 CWE를 포함합니다.


## 방법론 (Methodology)

이번 Top 10 버전은 데이터 기반이지만 맹목적으로 데이터 주도적이지는 않습니다. 우리는 기여된 데이터를 기반으로 12개 카테고리를 순위화했으며, 커뮤니티 설문조사 응답에 의해 두 개가 승격되거나 강조될 수 있도록 허용했습니다. 우리가 이렇게 하는 근본적인 이유는 다음과 같습니다: 기여된 데이터를 검토하는 것은 본질적으로 과거를 들여다보는 것입니다. 애플리케이션 보안 연구자들은 새로운 취약점을 식별하고 새로운 테스트 방법을 개발하는 데 시간을 투자합니다. 이러한 테스트를 도구와 프로세스에 통합하는 데는 몇 주에서 몇 년이 걸립니다. 우리가 규모로 약점을 신뢰성 있게 테스트할 수 있을 때쯤이면 몇 년이 지났을 수 있습니다. 또한 우리가 신뢰성 있게 테스트할 수 없고 데이터에 존재할 수 없는 중요한 위험도 있습니다. 이러한 관점을 균형 있게 조정하기 위해, 우리는 커뮤니티 설문조사를 사용하여 최전선의 애플리케이션 보안 및 개발 실무자들에게 테스트 데이터에서 과소 대표될 수 있는 필수 위험으로 보는 것에 대해 묻습니다.


## 카테고리 구조 방식 (How the categories are structured)

OWASP Top 10의 이전 버전에서 몇 가지 카테고리가 변경되었습니다. 다음은 카테고리 변경 사항에 대한 높은 수준의 요약입니다.

이번 반복에서 우리는 2021년 버전에서 했던 것처럼 CWE에 대한 제한 없이 데이터를 요청했습니다. 우리는 주어진 연도(2021년부터 시작)에 대해 테스트된 애플리케이션 수와 테스트에서 발견된 CWE의 인스턴스가 하나 이상 있는 애플리케이션 수를 요청했습니다. 이 형식을 통해 각 CWE가 애플리케이션 집단 내에서 얼마나 널리 퍼져 있는지 추적할 수 있습니다. 우리는 목적상 빈도를 무시합니다. 다른 상황에서는 필요할 수 있지만, 애플리케이션 집단의 실제 유병률만 숨깁니다. 애플리케이션이 CWE의 인스턴스를 4개 가지고 있든 4,000개 가지고 있든 Top 10 계산의 일부가 아닙니다. 특히 수동 테스터는 애플리케이션에서 반복되는 횟수에 관계없이 취약점을 한 번만 나열하는 경향이 있는 반면, 자동화된 테스트 프레임워크는 취약점의 모든 인스턴스를 고유한 것으로 나열하기 때문입니다. 우리는 2017년의 약 30개 CWE에서 2021년의 거의 400개 CWE로, 이번 버전에서 데이터셋에서 분석할 589개 CWE로 증가했습니다. 우리는 향후 보완 자료로 추가 데이터 분석을 수행할 계획입니다. CWE 수의 이러한 상당한 증가는 카테고리가 구조화되는 방식의 변경을 필요로 합니다.

우리는 몇 달 동안 CWE를 그룹화하고 분류했으며 추가로 몇 달 더 계속할 수 있었습니다. 어느 시점에서 멈춰야 했습니다. 근본 원인과 증상 유형의 CWE가 모두 있으며, 근본 원인 유형은 "암호화 실패(Cryptographic Failure)" 및 "설정 오류(Misconfiguration)"와 같은 반면 증상 유형은 "민감한 데이터 노출(Sensitive Data Exposure)" 및 "서비스 거부(Denial of Service)"와 대조됩니다. 우리는 식별 및 수정 가이드를 제공하는 데 더 논리적이기 때문에 가능할 때마다 근본 원인에 초점을 맞추기로 결정했습니다. 증상보다 근본 원인에 초점을 맞추는 것은 새로운 개념이 아닙니다. Top 10은 증상과 근본 원인의 혼합이었습니다. CWE도 증상과 근본 원인의 혼합입니다. 우리는 단순히 이를 더 의도적으로 지적하고 있습니다. 이번 버전에서 카테고리당 평균 25개의 CWE가 있으며, 하한은 A02:2025-소프트웨어 공급망 실패(Software Supply Chain Failures) 및 A09:2025 로깅 및 알림 실패(Logging and Alerting Failures)의 5개 CWE에서 A01:2025-접근 제어 취약점(Broken Access Control)의 40개 CWE까지입니다. 우리는 카테고리의 CWE 수를 40개로 제한하기로 결정했습니다. 이 업데이트된 카테고리 구조는 회사가 언어/프레임워크에 맞는 CWE에 집중할 수 있기 때문에 추가적인 교육 이점을 제공합니다. 

우리는 왜 MITRE Top 25 Most Dangerous Software Weaknesses와 유사하게 Top 10으로 10개 CWE 목록으로 전환하지 않는지 물어봤습니다. 우리가 카테고리에서 여러 CWE를 사용하는 주요 이유는 두 가지입니다. 첫째, 모든 CWE가 모든 프로그래밍 언어나 프레임워크에 존재하는 것은 아닙니다. 이는 도구 및 교육/인식 프로그램에 문제를 일으키며, Top 10의 일부가 적용되지 않을 수 있습니다. 두 번째 이유는 일반적인 취약점에 대해 여러 CWE가 있다는 것입니다. 예를 들어, 일반 인젝션(General Injection), 명령 인젝션(Command Injection), 크로스 사이트 스크립팅(Cross-site Scripting), 하드코딩된 암호(Hardcoded Passwords), 검증 부족(Lack of Validation), 버퍼 오버플로우(Buffer Overflows), 민감한 정보의 평문 저장(Cleartext Storage of Sensitive Information) 및 기타 많은 것에 대해 여러 CWE가 있습니다. 조직이나 테스터에 따라 다른 CWE가 사용될 수 있습니다. 여러 CWE가 있는 카테고리를 사용함으로써 우리는 공통 카테고리 이름 아래에서 발생할 수 있는 다양한 유형의 약점에 대한 기준선과 인식을 높이는 데 도움을 줄 수 있습니다. Top 10 2025 버전에서는 10개 카테고리 내에 248개의 CWE가 있습니다. 이번 릴리스 시점에 [MITRE의 다운로드 가능한 사전](https://cwe.mitre.org)에는 총 968개의 CWE가 있습니다.


## 카테고리 선택에 데이터 사용 방식 (How the data is used for selecting categories)

2021년 버전에서 했던 것과 유사하게, 우리는 *악용 가능성(Exploitability)* 및 *(기술적) 영향((Technical) Impact)*에 대한 CVE 데이터를 활용했습니다. 우리는 OWASP Dependency Check를 다운로드하고 CVSS 악용 및 영향 점수를 추출하여 CVE와 함께 나열된 관련 CWE별로 그룹화했습니다. 모든 CVE가 CVSSv2 점수를 가지고 있지만 CVSSv2에는 CVSSv3이 해결해야 할 결함이 있기 때문에 상당한 연구와 노력이 필요했습니다. 특정 시점 이후 모든 CVE에는 CVSSv3 점수도 할당됩니다. 또한 점수 범위와 공식이 CVSSv2와 CVSSv3 사이에서 업데이트되었습니다.

CVSSv2에서는 악용(Exploit)과 (기술적) 영향((Technical) Impact) 모두 최대 10.0까지 가능했지만, 공식은 악용에 대해 60%, 영향에 대해 40%로 낮췄습니다. CVSSv3에서는 이론적 최대값이 악용에 대해 6.0, 영향에 대해 4.0으로 제한되었습니다. 가중치를 고려하면, 영향 점수가 더 높게 이동했으며 CVSSv3에서 평균적으로 거의 1.5점 정도 높아졌고, 악용 가능성은 평균적으로 거의 0.5점 낮아졌습니다.

국가 취약점 데이터베이스(National Vulnerability Database, NVD)에서 OWASP Dependency Check에서 추출한 CWE에 매핑된 약 175k개의 CVE 레코드(2021년의 125k에서 증가)가 있습니다. 또한 CVE에 매핑된 643개의 고유 CWE(2021년의 241에서 증가)가 있습니다. 추출된 거의 220k개의 CVE 내에서 160k개는 CVSS v2 점수를 가지고, 156k개는 CVSS v3 점수를 가지고, 6k개는 CVSS v4 점수를 가지고 있습니다. 많은 CVE가 여러 점수를 가지고 있어 총합이 220k보다 많습니다.

Top 10 2025의 경우, 우리는 다음과 같은 방식으로 평균 악용 및 영향 점수를 계산했습니다. 우리는 CWE별로 CVSS 점수가 있는 모든 CVE를 그룹화하고, CVSSv3을 가진 인구의 비율뿐만 아니라 CVSSv2 점수를 가진 나머지 인구로 악용 및 영향 점수를 모두 가중하여 전체 평균을 얻었습니다. 우리는 이러한 평균을 데이터셋의 CWE에 매핑하여 위험 방정식의 다른 절반에 대한 악용 및 (기술적) 영향 점수로 사용했습니다.

왜 CVSS v4.0을 사용하지 않느냐고 물을 수 있습니다. 그것은 점수 알고리즘이 근본적으로 변경되었고, 더 이상 CVSS v2와 CVSSv3처럼 *악용(Exploit)* 또는 *영향(Impact)* 점수를 쉽게 제공하지 않기 때문입니다. 우리는 Top 10의 향후 버전에 대해 CVSS v4.0 점수를 사용하는 방법을 찾으려고 시도할 것이지만, 2025 버전에 대해 이를 수행할 시기적절한 방법을 결정할 수 없었습니다.


## 커뮤니티 설문조사를 사용하는 이유 (Why we use a community survey)

데이터의 결과는 업계가 자동화된 방식으로 테스트할 수 있는 것에 크게 제한됩니다. 숙련된 AppSec 전문가와 이야기하면, 그들은 데이터에 아직 없는 것들을 발견하고 추세를 보는 것에 대해 말할 것입니다. 특정 취약점 유형에 대한 테스트 방법론을 개발하는 데 시간이 걸리고, 그런 다음 이러한 테스트가 자동화되고 대규모 애플리케이션 집단에 대해 실행되는 데 더 많은 시간이 걸립니다. 우리가 찾는 모든 것은 과거를 되돌아보는 것이며, 데이터에 없는 지난해의 추세를 놓칠 수 있습니다.

따라서 우리는 데이터가 불완전하기 때문에 10개 카테고리 중 8개만 데이터에서 선택합니다. 다른 두 카테고리는 Top 10 커뮤니티 설문조사에서 나옵니다. 이를 통해 최전선의 실무자들이 데이터에 없을 수 있고(데이터로 표현되지 않을 수도 있음) 최고 위험으로 보는 것에 투표할 수 있습니다.


## 데이터 기여자에게 감사드립니다 (Thank you to our data contributors)

다음 조직들(여러 익명 기부자와 함께)은 280만 개 이상의 애플리케이션에 대한 데이터를 친절히 기부하여 이를 가장 크고 포괄적인 애플리케이션 보안 데이터셋으로 만들었습니다. 여러분 없이는 이것이 불가능했을 것입니다.

* Accenture (Prague)
* Anonymous (multiple)
* Bugcrowd
* Contrast Security
* CryptoNet Labs
* Intuitor SoftTech Services
* Orca Security
* Probley
* Semgrep
* Sonar
* usd AG
* Veracode
* Wallarm

## 주요 저자 (Lead Authors)
* Andrew van der Stock - X: [@vanderaj](https://x.com/vanderaj)
* Brian Glas - X: [@infosecdad](https://x.com/infosecdad)
* Neil Smithline - X: [@appsecneil](https://x.com/appsecneil)
* Tanya Janca - X: [@shehackspurple](https://x.com/shehackspurple)
* Torsten Gigler - Mastodon: [@torsten_gigler@infosec.exchange](https://infosec.exchange/@torsten_gigler)



## 릴리스 후보 (Release Candidate)


이 릴리스 후보는 원래 2025년 11월 6일에 릴리스되었습니다.


## 이슈 및 풀 리퀘스트 기록 (Log issues and pull requests)

모든 수정 사항이나 이슈를 기록해 주세요:

### 프로젝트 링크 (Project links):
* [홈페이지 (Homepage)](https://owasp.org/www-project-top-ten/)
* [GitHub 저장소 (GitHub repository)](https://github.com/OWASP/Top10)

