<link rel="stylesheet" href="../assets/css/RC-stylesheet.css" />

# A03:2025 소프트웨어 공급망 실패 (Software Supply Chain Failures) 


## 배경 (Background). 

이것은 Top 10 커뮤니티 설문조사에서 정확히 50%의 응답자가 #1로 순위를 매긴 최고 순위였습니다. 2013 Top 10에서 "A9 – 알려진 취약점이 있는 구성 요소 사용 (Using Components with Known Vulnerabilities)"으로 처음 등장한 이후, 이 위험은 알려진 취약점을 포함하는 것뿐만 아니라 모든 공급망 실패를 포함하도록 범위가 확장되었습니다. 이러한 범위 확대에도 불구하고, 공급망 실패는 관련 CWE를 가진 공통 취약점 및 노출(Common Vulnerability and Exposures, CVE)이 11개에 불과하여 식별하기 어려운 과제로 남아 있습니다. 그러나 기여된 데이터에서 테스트되고 보고될 때, 이 카테고리는 평균 발생률이 5.19%로 가장 높습니다. 관련 CWE는 *CWE-477: 사용 중단된 함수 사용 (Use of Obsolete Function), CWE-1104: 유지보수되지 않는 타사 구성 요소 사용 (Use of Unmaintained Third Party Components)*, CWE-1329: *업데이트할 수 없는 구성 요소에 대한 의존 (Reliance on Component That is Not Updateable)*, *CWE-1395: 취약한 타사 구성 요소에 대한 의존 (Dependency on Vulnerable Third-Party Component)*입니다.


## 점수 표 (Score table).


<table>
  <tr>
   <td>매핑된 CWE (CWEs Mapped) 
   </td>
   <td>최대 발생률 (Max Incidence Rate)
   </td>
   <td>평균 발생률 (Avg Incidence Rate)
   </td>
   <td>최대 커버리지 (Max Coverage)
   </td>
   <td>평균 커버리지 (Avg Coverage)
   </td>
   <td>평균 가중 악용 (Avg Weighted Exploit)
   </td>
   <td>평균 가중 영향 (Avg Weighted Impact)
   </td>
   <td>총 발생 횟수 (Total Occurrences)
   </td>
   <td>총 CVE (Total CVEs)
   </td>
  </tr>
  <tr>
   <td>5
   </td>
   <td>8.81%
   </td>
   <td>5.19%
   </td>
   <td>65.42%
   </td>
   <td>28.93%
   </td>
   <td>8.17
   </td>
   <td>5.23
   </td>
   <td>215,248
   </td>
   <td>11
   </td>
  </tr>
</table>



## 설명 (Description). 

소프트웨어 공급망 실패는 소프트웨어를 구축, 배포 또는 업데이트하는 과정에서 발생하는 고장 또는 기타 손상입니다. 이는 종종 시스템이 의존하는 타사 코드, 도구 또는 기타 종속성의 취약점이나 악의적인 변경으로 인해 발생합니다.

다음과 같은 경우 취약할 수 있습니다:

* 사용하는 모든 구성 요소(클라이언트 측 및 서버 측 모두)의 버전을 주의 깊게 추적하지 않는 경우. 여기에는 직접 사용하는 구성 요소뿐만 아니라 중첩된(전이적) 종속성이 포함됩니다.
* 소프트웨어가 취약하거나 지원되지 않거나 오래된 경우. 여기에는 OS, 웹/애플리케이션 서버, 데이터베이스 관리 시스템(DBMS), 애플리케이션, API 및 모든 구성 요소, 런타임 환경, 라이브러리가 포함됩니다.
* 취약점을 정기적으로 스캔하지 않고 사용하는 구성 요소와 관련된 보안 공지를 구독하지 않는 경우.
* 공급망 내 변경 사항에 대한 변경 관리 프로세스나 추적이 없는 경우. 여기에는 IDE, IDE 확장 및 업데이트 추적, 조직의 코드 저장소 변경, 샌드박스, 이미지 및 라이브러리 저장소, 아티팩트가 생성되고 저장되는 방식 등이 포함됩니다. 공급망의 모든 부분은 문서화되어야 하며, 특히 변경 사항은 그렇습니다.
* 공급망의 모든 부분을 강화하지 않은 경우. 특히 접근 제어와 최소 권한 적용에 중점을 둡니다. 
* 공급망 시스템에 업무 분리(separation of duty)가 없는 경우. 한 사람이 다른 사람의 감독 없이 코드를 작성하고 프로덕션까지 승격시킬 수 없어야 합니다.
* 개발자, DevOps 또는 인프라 전문가가 프로덕션에서 사용하기 위해 신뢰할 수 없는 소스에서 구성 요소를 다운로드하고 사용할 수 있는 경우.
* 기본 플랫폼, 프레임워크 및 종속성을 위험 기반으로 시기적절하게 수정하거나 업그레이드하지 않는 경우. 이것은 패치가 변경 제어 하에 월별 또는 분기별 작업인 환경에서 일반적으로 발생하며, 취약점을 수정하기 전에 조직을 며칠 또는 몇 달 동안 불필요한 노출에 노출시킵니다.
* 소프트웨어 개발자가 업데이트, 업그레이드 또는 패치된 라이브러리의 호환성을 테스트하지 않는 경우.
* 시스템의 모든 부분의 구성을 보안하지 않는 경우(참조 [A02:2025-보안 설정 오류 (Security Misconfiguration)](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)).
* 많은 구성 요소를 사용하지만 애플리케이션의 나머지 부분보다 보안이 약한 복잡한 CI/CD 파이프라인이 있는 경우.


## 예방 방법 (How to prevent). 

다음을 위한 패치 관리 프로세스가 있어야 합니다:



* 전체 소프트웨어의 소프트웨어 제품 구성 목록(Software Bill of Materials, SBOM)을 알고 SBOM 사전을 중앙에서 관리하세요.
* 자신의 종속성뿐만 아니라 그들의 (전이적) 종속성 등을 추적하세요.
* 사용하지 않는 종속성, 불필요한 기능, 구성 요소, 파일 및 문서를 제거하세요. 공격 표면 감소.
* versions, OWASP Dependency Check, retire.js 등의 도구를 사용하여 클라이언트 측 및 서버 측 구성 요소(예: 프레임워크, 라이브러리) 및 해당 종속성의 버전을 지속적으로 인벤토리하세요.
* 사용하는 구성 요소의 취약점에 대해 공통 취약점 및 노출(Common Vulnerability and Exposures, CVE) 및 국가 취약점 데이터베이스(National Vulnerability Database, NVD)와 같은 소스를 지속적으로 모니터링하세요. 소프트웨어 구성 분석, 소프트웨어 공급망 또는 보안 중심 SBOM 도구를 사용하여 프로세스를 자동화하세요. 사용하는 구성 요소와 관련된 보안 취약점에 대한 이메일 알림을 구독하세요.
* 안전한 링크를 통해 공식(신뢰할 수 있는) 소스에서만 구성 요소를 얻으세요. 수정되거나 악의적인 구성 요소를 포함할 가능성을 줄이기 위해 서명된 패키지를 선호하세요(참조 [A08:2025-소프트웨어 및 데이터 무결성 실패 (Software and Data Integrity Failures)](https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/)).
* 사용하는 종속성의 버전을 의도적으로 선택하고 필요할 때만 업그레이드하세요.
* 유지보수되지 않거나 이전 버전에 대한 보안 패치를 만들지 않는 라이브러리 및 구성 요소를 모니터링하세요. 패치가 불가능한 경우, 발견된 문제를 모니터링, 탐지 또는 보호하기 위해 가상 패치를 배포하는 것을 고려하세요.
* CI/CD, IDE 및 기타 개발자 도구를 정기적으로 업데이트하세요.
* CI/CD 파이프라인의 구성 요소를 이 프로세스의 일부로 취급하세요. 강화하고, 모니터링하고, 그에 따라 변경 사항을 문서화하세요.


다음에 대한 변경 사항을 추적하기 위한 변경 관리 프로세스 또는 추적 시스템이 있어야 합니다:
* CI/CD 설정(모든 빌드 도구 및 파이프라인)
* 코드 저장소
* 샌드박스 영역
* 개발자 IDE
* SBOM 도구 및 생성된 아티팩트
* 로깅 시스템 및 로그
* SaaS와 같은 타사 통합
* 아티팩트 저장소 
* 컨테이너 레지스트리


다음 시스템을 강화하세요. 여기에는 MFA 활성화 및 IAM 잠금이 포함됩니다:
* 코드 저장소(시크릿 체크인 방지, 브랜치 보호, 백업 포함)
* 개발자 워크스테이션(정기 패치, MFA, 모니터링 등)
* 빌드 서버 및 CI/CD(업무 분리, 접근 제어, 서명된 빌드, 환경 범위 시크릿, 변조 증거 로그 등)
* 아티팩트(출처, 서명 및 타임스탬프를 통한 무결성 보장, 각 환경에 대해 재구축하는 대신 아티팩트 승격, 빌드가 불변인지 확인)
* 코드로서의 인프라는 PR 사용 및 버전 제어를 포함하여 모든 코드처럼 관리됩니다.

모든 조직은 애플리케이션 또는 포트폴리오의 수명 동안 모니터링, 분류 및 업데이트 또는 구성 변경 적용을 위한 지속적인 계획을 보장해야 합니다.


## 공격 시나리오 예 (Example attack scenarios). 

**시나리오 #1:** 신뢰할 수 있는 벤더가 맬웨어로 손상되어 업그레이드할 때 컴퓨터 시스템이 손상됩니다. 가장 유명한 예는 아마도:

* 약 18,000개 조직이 손상된 2019년 SolarWinds 손상입니다. [https://www.npr.org/2021/04/16/985439655/a-worst-nightmare-cyberattack-the-untold-story-of-the-solarwinds-hack](https://www.npr.org/2021/04/16/985439655/a-worst-nightmare-cyberattack-the-untold-story-of-the-solarwinds-hack)

**시나리오 #2:** 신뢰할 수 있는 벤더가 특정 조건에서만 악의적으로 동작하도록 손상됩니다. 

* 2025년 Bybit의 15억 달러 도난은 대상 지갑이 사용될 때만 실행되는 지갑 소프트웨어의 공급망 공격으로 인해 발생했습니다. https://thehackernews.com/2025/02/bybit-hack-traced-to-safewallet-supply.html

**시나리오 #3:** VS Code 마켓플레이스에 대한 2025년 GlassWorm 공급망 공격은 악의적인 행위자가 VS 마켓플레이스의 합법적인 확장 프로그램과 OpenVSX 마켓플레이스의 여러 확장 프로그램에 보이지 않는 자가 복제 코드를 구현하여 개발자 머신에 자동 업데이트되었습니다. 웜은 즉시 개발자 머신에서 로컬 시크릿을 수집하고, 명령 및 제어를 설정하려고 시도했으며, 가능한 경우 개발자의 암호화폐 지갑을 비웠습니다. 이 공급망 공격은 매우 고급이고 빠르게 확산되며 손상이 컸으며, 개발자 머신을 대상으로 하여 개발자 자신이 이제 공급망 공격의 주요 대상임을 보여주었습니다.

**시나리오 #4:** 구성 요소는 일반적으로 애플리케이션 자체와 동일한 권한으로 실행되므로 모든 구성 요소의 결함이 심각한 영향을 초래할 수 있습니다. 이러한 결함은 우발적일 수 있습니다(예: 코딩 오류) 또는 의도적일 수 있습니다(예: 구성 요소의 백도어). 발견된 악용 가능한 구성 요소 취약점의 일부 예는 다음과 같습니다:


* CVE-2017-5638, 서버에서 임의 코드 실행을 가능하게 하는 Struts 2 원격 코드 실행 취약점은 심각한 침해의 원인으로 비난받았습니다.
* 사물 인터넷(Internet of Things, IoT)은 패치하기가 어렵거나 불가능한 경우가 많지만, 패치하는 것의 중요성은 클 수 있습니다(예: 생체의학 장치).

공격자가 패치되지 않았거나 잘못 구성된 시스템을 찾는 데 도움이 되는 자동화된 도구가 있습니다. 예를 들어, [Shodan IoT](https://www.shodan.io) 검색 엔진은 2014년 4월에 패치된 Heartbleed 취약점으로 여전히 고통받는 장치를 찾는 데 도움이 될 수 있습니다.

## 참고 자료 (References)

* [OWASP 애플리케이션 보안 검증 표준: V15 보안 코딩 및 아키텍처 (OWASP Application Security Verification Standard: V15 Secure Coding and Architecture)](https://owasp.org/www-project-application-security-verification-standard/)
* [OWASP 치트 시트 시리즈: 종속성 그래프 SBOM (OWASP Cheat Sheet Series: Dependency Graph SBOM)](https://cheatsheetseries.owasp.org/cheatsheets/Dependency_Graph_SBOM_Cheat_Sheet.html)
* [OWASP 치트 시트 시리즈: 취약한 종속성 관리 (OWASP Cheat Sheet Series: Vulnerable Dependency Management)](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html)
* [OWASP Dependency-Track](https://owasp.org/www-project-dependency-track/)
* [OWASP CycloneDX](https://owasp.org/www-project-cyclonedx/)
* [OWASP 애플리케이션 보안 검증 표준: V1 아키텍처, 설계 및 위협 모델링 (OWASP Application Security Verification Standard: V1 Architecture, design and threat modelling)](https://owasp-aasvs.readthedocs.io/en/latest/v1.html)
* [OWASP Dependency Check (Java 및 .NET 라이브러리용)](https://owasp.org/www-project-dependency-check/)
* OWASP 테스트 가이드 - 애플리케이션 아키텍처 매핑 (OTG-INFO-010)
* [OWASP 가상 패칭 모범 사례 (OWASP Virtual Patching Best Practices)](https://owasp.org/www-community/Virtual_Patching_Best_Practices)
* [불안전한 라이브러리의 불행한 현실 (The Unfortunate Reality of Insecure Libraries)](https://www.scribd.com/document/105692739/JeffWilliamsPreso-Sm)
* [MITRE 공통 취약점 및 노출 (CVE) 검색](https://www.cve.org)
* [국가 취약점 데이터베이스 (NVD)](https://nvd.nist.gov)
* [알려진 취약한 JavaScript 라이브러리 탐지를 위한 Retire.js](https://retirejs.github.io/retire.js/)
* [GitHub Advisory Database](https://github.com/advisories)
* Ruby 라이브러리 보안 공지 데이터베이스 및 도구
* [SAFECode 소프트웨어 무결성 제어 (PDF)](https://safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf)
* [Glassworm 공급망 공격](https://thehackernews.com/2025/10/self-spreading-glassworm-infects-vs.html)
* [PhantomRaven 공급망 공격 캠페인](https://thehackernews.com/2025/10/phantomraven-malware-found-in-126-npm.html)


## 매핑된 CWE 목록 (List of Mapped CWEs)

* [CWE-447 사용 중단된 함수 사용 (Use of Obsolete Function)](https://cwe.mitre.org/data/definitions/447.html)

* [CWE-1035 2017 Top 10 A9: 알려진 취약점이 있는 구성 요소 사용 (2017 Top 10 A9: Using Components with Known Vulnerabilities)](https://cwe.mitre.org/data/definitions/1035.html)

* [CWE-1104 유지보수되지 않는 타사 구성 요소 사용 (Use of Unmaintained Third Party Components)](https://cwe.mitre.org/data/definitions/1104.html)

* [CWE-1329 업데이트할 수 없는 구성 요소에 대한 의존 (Reliance on Component That is Not Updateable)](https://cwe.mitre.org/data/definitions/1329.html)

* [CWE-1395 취약한 타사 구성 요소에 대한 의존 (Dependency on Vulnerable Third-Party Component)](https://cwe.mitre.org/data/definitions/1395.html)
