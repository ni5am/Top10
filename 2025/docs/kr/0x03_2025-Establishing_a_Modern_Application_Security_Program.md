<link rel="stylesheet" href="../../assets/css/RC-stylesheet.css" />

# 현대적 애플리케이션 보안 프로그램 수립 (Establishing a Modern Application Security Program)

OWASP Top 10 목록은 인식 문서로, 다루는 주제의 가장 중요한 위험에 대한 인식을 가져오기 위한 것입니다. 완전한 목록이 아니라 시작점일 뿐입니다. 이 목록의 이전 버전에서 우리는 이러한 위험과 더 많은 것을 피하는 최선의 방법으로 애플리케이션 보안 프로그램을 시작하는 것을 권장했습니다. 이 섹션에서는 현대적 애플리케이션 보안 프로그램을 시작하고 구축하는 방법을 다룹니다.

 

이미 애플리케이션 보안 프로그램이 있다면, [OWASP SAMM (소프트웨어 보증 성숙도 모델, Software Assurance Maturity Model)](https://owasp.org/www-project-samm/) 또는 DSOMM (DevSecOps 성숙도 모델, DevSecOps Maturity Model)을 사용하여 성숙도 평가를 수행하는 것을 고려하세요. 이러한 성숙도 모델은 포괄적이고 철저하며 프로그램을 확장하고 성숙시키기 위해 노력을 집중해야 할 곳을 파악하는 데 도움이 될 수 있습니다. 참고: OWASP SAMM 또는 DSOMM의 모든 것을 수행할 필요는 없습니다. 그들은 여러분을 안내하고 많은 옵션을 제공하기 위한 것입니다. 달성할 수 없는 표준이나 감당할 수 없는 프로그램을 제공하거나 설명하기 위한 것이 아닙니다. 많은 아이디어와 옵션을 제공하기 위해 광범위합니다.

 

프로그램을 처음부터 시작하거나, OWASP SAMM 또는 DSOMM이 현재 팀에게 '너무 많다'고 생각되면 다음 조언을 검토하세요.


### 1. 위험 기반 포트폴리오 접근 방식 수립 (Establish a Risk Based Portfolio Approach):

* 비즈니스 관점에서 애플리케이션 포트폴리오의 보호 요구 사항을 식별하세요. 이것은 보호되는 데이터 자산과 관련된 개인정보 보호법 및 기타 규정에 의해 부분적으로 구동되어야 합니다.

* 조직의 위험 허용도를 반영하는 일관된 가능성 및 영향 요소 세트를 가진 [공통 위험 평가 모델](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology)을 수립하세요.


* 이에 따라 모든 애플리케이션과 API를 측정하고 우선순위를 지정하세요. 결과를 [구성 관리 데이터베이스 (Configuration Management Database, CMDB)](https://de.wikipedia.org/wiki/Configuration_Management_Database)에 추가하세요.

* 커버리지와 필요한 엄격성 수준을 적절히 정의하는 보증 가이드라인을 수립하세요.


### 2. 강력한 기반으로 활성화 (Enable with a Strong Foundation):

* 모든 개발 팀이 준수할 애플리케이션 보안 기준선을 제공하는 집중된 정책 및 표준 세트를 수립하세요.

* 이러한 정책 및 표준을 보완하고 사용에 대한 설계 및 개발 가이드를 제공하는 재사용 가능한 보안 제어의 공통 세트를 정의하세요.

* 다양한 개발 역할 및 주제에 대해 필수이고 대상화된 애플리케이션 보안 교육 커리큘럼을 수립하세요.


### 3. 기존 프로세스에 보안 통합 (Integrate Security into Existing Processes):

* 기존 개발 및 운영 프로세스에 보안 구현 및 검증 활동을 정의하고 통합하세요.

* 활동에는 위협 모델링, 보안 설계 및 설계 검토, 보안 코딩 및 코드 검토, 침투 테스트, 수정이 포함됩니다.

* 개발 및 프로젝트 팀이 성공할 수 있도록 주제 전문가 및 지원 서비스를 제공하세요.

* 현재 시스템 개발 수명 주기 및 모든 소프트웨어 보안 활동, 도구, 정책, 프로세스를 검토한 다음 문서화하세요.

* 새로운 소프트웨어의 경우, 시스템 개발 수명 주기(System Development Life Cycle, SDLC)의 각 단계에 하나 이상의 보안 활동을 추가하세요. 아래에서 수행할 수 있는 많은 제안을 제공합니다. 모든 새 프로젝트나 소프트웨어 이니셔티브에서 이러한 새로운 활동을 수행하도록 하세요. 이렇게 하면 각 새로운 소프트웨어가 조직에 허용 가능한 보안 상태로 제공될 것임을 알 수 있습니다.

* 최종 제품이 조직에 허용 가능한 수준의 위험을 충족하도록 활동을 선택하세요.

* 기존 소프트웨어(때로는 레거시라고 함)의 경우 공식 유지보수 계획을 갖고 싶을 것입니다. '운영 및 변경 관리(Operations and Change Management)' 섹션에서 보안 애플리케이션을 유지하는 방법에 대한 아이디어를 참조하세요.


### 4. 애플리케이션 보안 교육 (Application Security Education):

* 개발자를 위한 보안 챔피언 프로그램 또는 일반 보안 교육 프로그램(때로는 옹호 또는 보안 인식 프로그램이라고 함)을 시작하는 것을 고려하여 그들이 알고 있기를 바라는 모든 것을 가르치세요. 이것은 그들을 최신 상태로 유지하고, 보안하게 작업하는 방법을 알게 하며, 작업하는 곳의 보안 문화를 더 긍정적으로 만듭니다. 또한 팀 간의 신뢰를 향상시키고 더 행복한 작업 관계를 만드는 경우가 많습니다. OWASP는 단계적으로 확장되고 있는 [OWASP 보안 챔피언 가이드 (OWASP Security Champions Guide)](https://securitychampions.owasp.org/)로 이를 지원합니다.

* OWASP 교육 프로젝트는 개발자에게 웹 애플리케이션 보안에 대해 교육하는 데 도움이 되는 교육 자료를 제공합니다. 취약점에 대한 실습 학습을 위해 [OWASP Juice Shop 프로젝트](https://owasp.org/www-project-juice-shop/) 또는 [OWASP WebGoat](https://owasp.org/www-project-webgoat/)를 시도해보세요. 최신 상태를 유지하려면 [OWASP AppSec 컨퍼런스](https://owasp.org/events/), [OWASP 컨퍼런스 교육](https://owasp.org/events/), 또는 지역 [OWASP 챕터](https://owasp.org/chapters/) 모임에 참석하세요.


### 5. 관리 가시성 제공 (Provide Management Visibility):

* 메트릭으로 관리하세요. 캡처된 메트릭 및 분석 데이터를 기반으로 개선 및 자금 조달 결정을 추진하세요. 메트릭에는 보안 관행 및 활동 준수, 도입된 취약점, 완화된 취약점, 애플리케이션 커버리지, 유형별 및 인스턴스 수별 결함 밀도 등이 포함됩니다.

* 구현 및 검증 활동의 데이터를 분석하여 근본 원인 및 취약점 패턴을 찾아 전사적으로 전략적이고 체계적인 개선을 추진하세요. 실수로부터 배우고 개선을 촉진하기 위한 긍정적인 인센티브를 제공하세요.



## 반복 가능한 보안 프로세스 및 표준 보안 제어 수립 및 사용 (Establish & Use Repeatable Security Processes and Standard Security Controls)

### 요구 사항 및 리소스 관리 단계 (Requirements and Resource Management Phase):

* 비즈니스와 함께 애플리케이션에 대한 비즈니스 요구 사항을 수집하고 협상하세요. 여기에는 모든 데이터 자산의 기밀성, 진정성, 무결성 및 가용성에 관한 보호 요구 사항과 예상 비즈니스 로직이 포함됩니다.

* 기능적 및 비기능적 보안 요구 사항을 포함한 기술 요구 사항을 컴파일하세요. OWASP는 애플리케이션의 보안 요구 사항을 설정하기 위한 가이드로 [OWASP 애플리케이션 보안 검증 표준 (Application Security Verification Standard, ASVS)](https://owasp.org/www-project-application-security-verification-standard/)을 사용하는 것을 권장합니다.

* 설계, 구축, 테스트 및 운영의 모든 측면을 포함하는 예산을 계획하고 협상하세요. 여기에는 보안 활동이 포함됩니다.

* 프로젝트 일정에 보안 활동을 추가하세요.

* 프로젝트 킥오프에서 보안 담당자로 자신을 소개하여 누구에게 이야기해야 하는지 알 수 있도록 하세요.


### 제안 요청서 (RFP) 및 계약 (Request for Proposals (RFP) and Contracting):

* 내부 또는 외부 개발자와 요구 사항을 협상하세요. 여기에는 보안 프로그램에 관한 가이드라인 및 보안 요구 사항(예: SDLC, 모범 사례)이 포함됩니다.

*  계획 및 설계 단계를 포함하여 모든 기술 요구 사항의 이행을 평가하세요.

*  설계, 보안 및 서비스 수준 계약(Service Level Agreement, SLA)을 포함한 모든 기술 요구 사항을 협상하세요.

*  [OWASP 보안 소프트웨어 계약 부록(1) (OWASP Secure Software Contract Annex)](https://owasp.org/www-community/OWASP_Secure_Software_Contract_Annex)과 같은 템플릿 및 체크리스트를 채택하세요.<br>** 1: 참고** *부록은 미국 계약법용이므로 샘플 부록을 사용하기 전에 자격을 갖춘 법률 자문을 상담하세요.*


### 계획 및 설계 단계 (Planning and Design Phase):

*  개발자 및 내부 이해관계자(예: 보안 전문가)와 계획 및 설계를 협상하세요.

* 보호 요구 사항 및 예상 위협 수준에 적합한 보안 아키텍처, 제어, 대응 조치 및 설계 검토를 정의하세요. 이것은 보안 전문가의 지원을 받아야 합니다.

* 애플리케이션 및 API에 보안을 나중에 추가하는 것보다 처음부터 보안을 설계하는 것이 훨씬 더 비용 효율적입니다. OWASP는 처음부터 보안을 포함하도록 설계하는 방법에 대한 가이드의 좋은 시작점으로 [OWASP 치트 시트 (OWASP Cheat Sheets)](https://cheatsheetseries.owasp.org/index.html)와 [OWASP 사전 대응 제어 (OWASP Proactive Controls)](https://top10proactive.owasp.org/)를 권장합니다.

*  위협 모델링을 수행하세요. [OWASP 치트 시트: 위협 모델링 (OWASP Cheat Sheet: Threat Modeling)](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)을 참조하세요.

*  소프트웨어 아키텍트에게 보안 설계 개념 및 패턴을 가르치고 가능한 경우 설계에 추가하도록 요청하세요.

*  개발자와 함께 데이터 흐름을 검토하세요.

*  다른 모든 사용자 스토리와 함께 보안 사용자 스토리를 추가하세요.


### 보안 개발 수명 주기 (Secure Development Lifecycle):


* 조직이 애플리케이션 및 API를 구축할 때 따르는 프로세스를 개선하기 위해 OWASP는 [OWASP 소프트웨어 보증 성숙도 모델 (Software Assurance Maturity Model, SAMM)](https://owasp.org/www-project-samm/)을 권장합니다. 이 모델은 조직이 조직이 직면한 특정 위험에 맞춤화된 소프트웨어 보안 전략을 수립하고 구현하는 데 도움이 됩니다.

*  소프트웨어 개발자에게 보안 코딩 교육 및 더 강력하고 보안한 애플리케이션을 만드는 데 도움이 될 것으로 생각하는 기타 교육을 제공하세요.

*  코드 검토를 수행하세요. [OWASP 치트 시트: 보안 코드 검토 (OWASP Cheat Sheet: Secure Code Review)](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Code_Review_Cheat_Sheet.html)를 참조하세요.

*  개발자에게 보안 도구를 제공한 다음 사용 방법을 가르치세요. 특히 정적 분석, 소프트웨어 구성 분석, 시크릿, [코드로서의 인프라 (Infrastructure-as-Code, IaC)](https://cheatsheetseries.owasp.org/cheatsheets/Infrastructure_as_Code_Security_Cheat_Sheet.html) 스캐너를 포함합니다.

*  가능한 경우 개발자를 위한 가드레일을 만드세요(더 안전한 선택을 향해 이끄는 기술적 안전장치).

*   강력하고 사용 가능한 보안 제어를 구축하는 것은 어렵습니다. 가능할 때마다 보안 기본값을 제공하고, 가능할 때마다 '포장된 도로(paved roads)'를 만드세요(가장 쉬운 방법을 가장 안전한 방법으로 만드는 것, 명백한 선호 방법). [OWASP 치트 시트 (OWASP Cheat Sheets)](https://cheatsheetseries.owasp.org/index.html)는 개발자를 위한 좋은 시작점이며, 많은 현대 프레임워크가 이제 인증, 검증, CSRF 방지 등을 위한 표준 및 효과적인 보안 제어와 함께 제공됩니다.

*  개발자에게 보안 관련 IDE 플러그인을 제공하고 사용을 권장하세요.

*  시크릿 관리 도구, 라이선스 및 사용 방법에 대한 문서를 제공하세요.

*  이상적으로는 유용한 보안 문서로 가득 찬 RAG 서버, 더 나은 결과를 위해 팀이 작성한 프롬프트, 조직의 선택한 보안 도구를 호출하는 MCP 서버로 설정된 프라이빗 AI를 제공하세요. 그들이 원하든 원하지 않든 할 것이기 때문에 AI를 안전하게 사용하는 방법을 가르치세요.


### 지속적인 애플리케이션 보안 테스트 수립 (Establish Continuous Application Security Testing):

*  기술 기능 및 IT 아키텍처와의 통합을 테스트하고 비즈니스 테스트를 조정하세요.

* 기술 및 비즈니스 관점에서 "사용" 및 "남용" 테스트 케이스를 만드세요.

* 내부 프로세스, 보호 요구 사항 및 애플리케이션별 가정된 위협 수준에 따라 보안 테스트를 관리하세요.

* 보안 테스트 도구(퍼저, DAST 등), 안전한 테스트 장소 및 사용 방법에 대한 교육을 제공하거나, 테스트를 대신 수행하거나, 테스터를 고용하세요.

*  높은 수준의 보증이 필요한 경우 공식 침투 테스트뿐만 아니라 스트레스 테스트 및 성능 테스트를 고려하세요.

*  개발자와 협력하여 버그 보고서에서 수정해야 할 사항을 결정하는 데 도움을 주고, 관리자가 이를 수행할 시간을 제공하도록 하세요.


### 롤아웃 (Rollout):

* 애플리케이션을 운영에 배치하고 필요한 경우 이전에 사용한 애플리케이션에서 마이그레이션하세요.

* 변경 관리 데이터베이스(CMDB) 및 보안 아키텍처를 포함한 모든 문서를 완료하세요.


### 운영 및 변경 관리 (Operations and Change Management):

*  운영에는 애플리케이션의 보안 관리에 대한 가이드라인(예: 패치 관리)이 포함되어야 합니다.

*  사용자의 보안 인식을 높이고 사용성 대 보안에 대한 갈등을 관리하세요.

*  변경 사항을 계획하고 관리하세요. 예: 애플리케이션 또는 OS, 미들웨어, 라이브러리와 같은 기타 구성 요소의 새 버전으로 마이그레이션.

*  모든 앱이 인벤토리에 있고 모든 중요한 세부 사항이 문서화되어 있는지 확인하세요. CMDB 및 보안 아키텍처, 제어 및 대응 조치를 포함한 모든 문서를 업데이트하세요. 여기에는 모든 런북 또는 프로젝트 문서가 포함됩니다.

*  모든 앱에 대해 로깅, 모니터링 및 알림을 수행하세요. 누락된 경우 추가하세요.

*  효과적이고 효율적인 업데이트 및 패치를 위한 프로세스를 만드세요.

*  정기적인 스캔 일정을 만드세요(바라건대 동적, 정적, 시크릿, IaC 및 소프트웨어 구성 분석).

*  보안 버그 수정을 위한 SLA.

*  직원(그리고 이상적으로는 고객도)이 버그를 보고할 수 있는 방법을 제공하세요.

*  소프트웨어 공격이 어떻게 보이는지 이해하는 훈련된 사고 대응 팀, 관찰 가능성 도구를 수립하세요.

*  자동화된 공격을 중지하기 위해 차단 또는 차폐 도구를 실행하세요.

*  구성의 연간(또는 더 자주) 강화.

*  최소한 연간 침투 테스트(앱에 필요한 보증 수준에 따라).

*  소프트웨어 공급망을 강화하고 보호하기 위한 프로세스 및 도구를 수립하세요.

*  가장 중요한 애플리케이션과 이를 유지하는 데 사용하는 도구를 포함하는 비즈니스 연속성 및 재해 복구 계획을 수립하고 업데이트하세요.


### 시스템 폐기 (Retiring Systems):

* 필요한 모든 데이터는 보관해야 합니다. 다른 모든 데이터는 안전하게 삭제해야 합니다.

* 사용하지 않는 계정, 역할 및 권한을 삭제하는 것을 포함하여 애플리케이션을 안전하게 폐기하세요.

* CMDB에서 애플리케이션의 상태를 폐기로 설정하세요.


## OWASP Top 10을 표준으로 사용 (Using the OWASP Top 10 as a standard)

OWASP Top 10은 주로 인식 문서입니다. 그러나 이것은 2003년 시작 이래 조직이 사실상의 업계 AppSec 표준으로 사용하는 것을 막지 못했습니다. OWASP Top 10을 코딩 또는 테스트 표준으로 사용하려면, 이것이 최소한이며 시작점일 뿐이라는 것을 알아야 합니다.

OWASP Top 10을 표준으로 사용하는 것의 어려움 중 하나는 우리가 AppSec 위험을 문서화하며, 반드시 쉽게 테스트 가능한 문제는 아니라는 것입니다. 예를 들어, [A06:2025-불안전한 설계 (Insecure Design)](A06_2025-Insecure_Design.md)는 대부분의 테스트 형태의 범위를 벗어납니다. 또 다른 예는 제자리에서, 사용 중이며 효과적인 로깅 및 모니터링이 구현되었는지 테스트하는 것으로, 이는 인터뷰와 효과적인 사고 대응 샘플 요청으로만 수행할 수 있습니다. 정적 코드 분석 도구는 로깅의 부재를 찾을 수 있지만, 비즈니스 로직이나 접근 제어가 중요한 보안 침해를 로깅하는지 확인하는 것은 불가능할 수 있습니다. 침투 테스터는 테스트 환경에서 사고 대응을 호출했다는 것만 확인할 수 있을 수 있으며, 이는 프로덕션과 같은 방식으로 모니터링되는 경우가 거의 없습니다.

OWASP Top 10을 사용하는 것이 적절한 경우에 대한 권장 사항은 다음과 같습니다:


<table>
  <tr>
   <td><strong>사용 사례 (Use Case)</strong>
   </td>
   <td><strong>OWASP Top 10 2025</strong>
   </td>
   <td><strong>OWASP 애플리케이션 보안 검증 표준 (OWASP Application Security Verification Standard)</strong>
   </td>
  </tr>
  <tr>
   <td>인식 (Awareness)
   </td>
   <td>예 (Yes)
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>교육 (Training)
   </td>
   <td>입문 수준 (Entry level)
   </td>
   <td>포괄적 (Comprehensive)
   </td>
  </tr>
  <tr>
   <td>설계 및 아키텍처 (Design and architecture)
   </td>
   <td>가끔 (Occasionally)
   </td>
   <td>예 (Yes)
   </td>
  </tr>
  <tr>
   <td>코딩 표준 (Coding standard)
   </td>
   <td>최소한 (Bare minimum)
   </td>
   <td>예 (Yes)
   </td>
  </tr>
  <tr>
   <td>보안 코드 검토 (Secure Code review)
   </td>
   <td>최소한 (Bare minimum)
   </td>
   <td>예 (Yes)
   </td>
  </tr>
  <tr>
   <td>동료 검토 체크리스트 (Peer review checklist)
   </td>
   <td>최소한 (Bare minimum)
   </td>
   <td>예 (Yes)
   </td>
  </tr>
  <tr>
   <td>단위 테스트 (Unit testing)
   </td>
   <td>가끔 (Occasionally)
   </td>
   <td>예 (Yes)
   </td>
  </tr>
  <tr>
   <td>통합 테스트 (Integration testing)
   </td>
   <td>가끔 (Occasionally)
   </td>
   <td>예 (Yes)
   </td>
  </tr>
  <tr>
   <td>침투 테스트 (Penetration testing)
   </td>
   <td>최소한 (Bare minimum)
   </td>
   <td>예 (Yes)
   </td>
  </tr>
  <tr>
   <td>도구 지원 (Tool support)
   </td>
   <td>최소한 (Bare minimum)
   </td>
   <td>예 (Yes)
   </td>
  </tr>
  <tr>
   <td>보안 공급망 (Secure Supply Chain)
   </td>
   <td>가끔 (Occasionally)
   </td>
   <td>예 (Yes)
   </td>
  </tr>
</table>


우리는 애플리케이션 보안 표준을 채택하려는 모든 사람에게 [OWASP 애플리케이션 보안 검증 표준 (OWASP Application Security Verification Standard)](https://owasp.org/www-project-application-security-verification-standard/) (ASVS)을 사용하도록 권장합니다. 검증 가능하고 테스트 가능하도록 설계되었으며 보안 개발 수명 주기의 모든 부분에서 사용할 수 있기 때문입니다.

ASVS는 도구 벤더에게 유일하게 허용되는 선택입니다. [A06:2025-불안전한 설계 (Insecure Design)](A06_2025-Insecure_Design.md)를 참조하여 여러 OWASP Top 10 위험의 특성으로 인해 도구가 OWASP Top 10을 포괄적으로 탐지, 테스트 또는 보호할 수 없습니다. OWASP는 OWASP Top 10의 완전한 커버리지에 대한 모든 주장을 권장하지 않습니다. 왜냐하면 단순히 사실이 아니기 때문입니다.
