<link rel="stylesheet" href="../../assets/css/RC-stylesheet.css" />

# 애플리케이션 보안 위험이란 무엇인가? (What are Application Security Risks?)
공격자는 잠재적으로 애플리케이션을 통해 비즈니스나 조직에 해를 끼칠 수 있는 많은 다른 경로를 사용할 수 있습니다. 이러한 각 방법은 조사가 필요한 잠재적 위험을 제기합니다.

![Calculation diagram](../assets/2025-algorithm-diagram.png)

<table>
  <tr>
   <td>
    <strong>위협 행위자 (Threat Agents)</strong>
   </td>
   <td>
    <strong>공격 벡터 (Attack \
Vectors)</strong>
   </td>
   <td>
    <strong>악용 가능성 (Exploitability)</strong>
   </td>
   <td>
    <strong>보안 제어 누락 가능성 (Likelihood of Missing Security</strong>
<p style="text-align: center">

    <strong>Controls)</strong>
   </td>
   <td>
    <strong>기술적 (Technical)</strong>
<p style="text-align: center">

    <strong>영향 (Impacts)</strong>
   </td>
   <td>
    <strong>비즈니스 (Business)</strong>
<p style="text-align: center">

    <strong>영향 (Impacts)</strong>
   </td>
  </tr>
  <tr>
   <td>
    <strong>환경별, \
상황 그림에 따라 동적</strong>
   </td>
   <td>
    <strong>애플리케이션 노출별 (환경별)</strong>
   </td>
   <td>
    <strong>평균 가중 악용 (Avg Weighted Exploit)</strong>
   </td>
   <td>
    <strong>평균 발생률로 가중된 \
커버리지별 누락 제어</strong>
   </td>
   <td>
    <strong>평균 가중 영향 (Avg Weighted Impact)</strong>
   </td>
   <td>
    <strong>비즈니스별</strong>
   </td>
  </tr>
</table>


우리의 위험 평가에서 우리는 악용 가능성, 약점에 대한 보안 제어 누락의 평균 가능성 및 기술적 영향의 보편적 매개변수를 고려했습니다. 

각 조직은 고유하며, 해당 조직에 대한 위협 행위자, 그들의 목표, 그리고 모든 침해의 영향도 마찬가지입니다. 공공 이익 조직이 공개 정보에 대해 콘텐츠 관리 시스템(Content Management System, CMS)을 사용하고 건강 시스템이 동일한 정확한 CMS를 민감한 건강 기록에 사용하는 경우, 동일한 소프트웨어에 대해 위협 행위자와 비즈니스 영향이 매우 다를 수 있습니다. 애플리케이션의 노출, 상황 그림에 따른 적용 가능한 위협 행위자(비즈니스 및 위치별 표적 및 비표적 공격), 그리고 개별 비즈니스 영향을 기반으로 조직에 대한 위험을 이해하는 것이 중요합니다. 


## 카테고리 선택 및 순위 지정에 데이터 사용 방식 (How the data is used for selecting categories and ranking them)

2017년에는 발생률로 카테고리를 선택하여 가능성을 결정한 다음, 수십 년의 경험을 바탕으로 악용 가능성(Exploitability), 탐지 가능성(Detectability, 가능성), 기술적 영향(Technical Impact)에 대한 팀 토론을 기반으로 순위를 지정했습니다. 2021년의 경우, 국가 취약점 데이터베이스(National Vulnerability Database, NVD)의 CVSSv2 및 CVSSv3 점수에서 악용 가능성(Exploitability) 및 (기술적) 영향((Technical) Impact)에 대한 데이터를 사용했습니다. 2025년의 경우, 우리는 2021년에 만든 동일한 방법론을 계속 사용했습니다.

우리는 OWASP Dependency Check를 다운로드하고 CVSS 악용 및 영향 점수를 추출하여 관련 CWE별로 그룹화했습니다. 모든 CVE가 CVSSv2 점수를 가지고 있지만 CVSSv2에는 CVSSv3이 해결해야 할 결함이 있기 때문에 상당한 연구와 노력이 필요했습니다. 특정 시점 이후 모든 CVE에는 CVSSv3 점수도 할당됩니다. 또한 점수 범위와 공식이 CVSSv2와 CVSSv3 사이에서 업데이트되었습니다. 

CVSSv2에서는 악용(Exploit)과 (기술적) 영향((Technical) Impact) 모두 최대 10.0까지 가능했지만, 공식은 악용에 대해 60%, 영향에 대해 40%로 낮췄습니다. CVSSv3에서는 이론적 최대값이 악용에 대해 6.0, 영향에 대해 4.0으로 제한되었습니다. 가중치를 고려하면, 영향 점수가 더 높게 이동했으며 CVSSv3에서 평균적으로 거의 1.5점 정도 높아졌고, 2021 Top 10에 대한 분석을 수행했을 때 악용 가능성은 평균적으로 거의 0.5점 낮아졌습니다.

국가 취약점 데이터베이스(NVD)에서 OWASP Dependency Check에서 추출한 CWE에 매핑된 약 175k개의 CVE 레코드(2021년의 125k에서 증가)가 있습니다. 또한 CVE에 매핑된 643개의 고유 CWE(2021년의 241에서 증가)가 있습니다. 추출된 거의 220k개의 CVE 내에서 160k개는 CVSS v2 점수를 가지고, 156k개는 CVSS v3 점수를 가지고, 6k개는 CVSS v4 점수를 가지고 있습니다. 많은 CVE가 여러 점수를 가지고 있어 총합이 220k보다 많습니다.

Top 10 2025의 경우, 우리는 다음과 같은 방식으로 평균 악용 및 영향 점수를 계산했습니다. 우리는 CWE별로 CVSS 점수가 있는 모든 CVE를 그룹화하고, CVSSv3을 가진 인구의 비율뿐만 아니라 CVSSv2 점수를 가진 나머지 인구로 악용 및 영향 점수를 모두 가중하여 전체 평균을 얻었습니다. 우리는 이러한 평균을 데이터셋의 CWE에 매핑하여 위험 방정식의 다른 절반에 대한 악용 및 (기술적) 영향 점수로 사용했습니다.

왜 CVSS v4.0을 사용하지 않느냐고 물을 수 있습니다. 그것은 점수 알고리즘이 근본적으로 변경되었고, 더 이상 CVSS v2와 CVSSv3처럼 *악용(Exploit)* 또는 *영향(Impact)* 점수를 쉽게 제공하지 않기 때문입니다. 우리는 Top 10의 향후 버전에 대해 CVSS v4.0 점수를 사용하는 방법을 찾으려고 시도할 것이지만, 2025 버전에 대해 이를 수행할 시기적절한 방법을 결정할 수 없었습니다.

발생률의 경우, 우리는 조직이 일정 기간 동안 테스트한 인구에서 각 CWE에 취약한 애플리케이션의 비율을 계산했습니다. 상기하자면, 우리는 빈도(또는 애플리케이션에서 문제가 나타나는 횟수)를 사용하지 않으며, 애플리케이션 인구의 몇 퍼센트가 각 CWE를 가지고 있는지에 관심이 있습니다. 

커버리지의 경우, 주어진 CWE에 대해 모든 조직이 테스트한 애플리케이션의 비율을 살펴봅니다. 계산된 커버리지가 높을수록 샘플 크기가 인구를 더 잘 대표하기 때문에 발생률이 정확하다는 보장이 더 강해집니다.

이번 반복에 사용한 공식은 2021년과 유사하며, 일부 가중치 변경이 있습니다:
(최대 발생률 % * 1000) + (최대 커버리지 % * 100) + (평균 악용 * 10) + (평균 영향 * 20) + (발생 합계 / 10000) = 위험 점수

계산된 점수는 접근 제어 취약점(Broken Access Control) 카테고리의 621.60에서 메모리 관리 오류(Memory Management Errors)의 271.08까지 범위였습니다.

이것은 완벽한 시스템이 아니지만 위험 카테고리 순위 지정에 가치가 있습니다.

점점 더 커지는 추가적인 도전 과제는 "애플리케이션"의 정의입니다. 업계가 마이크로서비스 및 기타 전통적인 애플리케이션보다 작은 구현으로 구성된 다른 아키텍처로 전환함에 따라 계산이 더 어려워집니다. 예를 들어, 조직이 코드 저장소를 테스트하는 경우, 애플리케이션으로 간주하는 것은 무엇입니까? CVSSv4의 성장과 유사하게, Top 10의 다음 버전은 지속적으로 변화하는 업계를 고려하기 위해 분석과 점수를 조정해야 할 수 있습니다.

## 데이터 요소 (Data Factors)

Top 10 카테고리 각각에 대해 나열된 데이터 요소가 있으며, 다음은 그 의미입니다:

**매핑된 CWE (CWEs Mapped):** Top 10 팀이 카테고리에 매핑한 CWE 수입니다.

**발생률 (Incidence Rate):** 발생률은 해당 연도에 해당 조직이 테스트한 인구에서 해당 CWE에 취약한 애플리케이션의 비율입니다.

**가중 악용 (Weighted Exploit):** CWE에 매핑된 CVE에 할당된 CVSSv2 및 CVSSv3 점수에서 악용 하위 점수로, 정규화되어 10점 척도에 배치됩니다.

**가중 영향 (Weighted Impact):** CWE에 매핑된 CVE에 할당된 CVSSv2 및 CVSSv3 점수에서 영향 하위 점수로, 정규화되어 10점 척도에 배치됩니다.

**(테스트) 커버리지 ((Testing) Coverage):** 주어진 CWE에 대해 모든 조직이 테스트한 애플리케이션의 비율입니다.

**총 발생 횟수 (Total Occurrences):** 카테고리에 매핑된 CWE를 가진 것으로 발견된 애플리케이션의 총 수입니다.

**총 CVE (Total CVEs):** 카테고리에 매핑된 CWE에 매핑된 CWE에 매핑된 NVD DB의 총 CVE 수입니다.

**공식 (Formula):** (최대 발생률 % * 1000) + (최대 커버리지 % * 100) + (평균 악용 * 10) + (평균 영향 * 20) + (발생 합계 / 10000) = 위험 점수
