/*
 * WorkshopSelector.h - Workshop Selection Interface
 */

#ifndef WORKSHOP_SELECTOR_H
#define WORKSHOP_SELECTOR_H

class PlanePilotApp;

class WorkshopSelector {
public:
    explicit WorkshopSelector(PlanePilotApp* app);
    ~WorkshopSelector();
    
    bool initialize();
    void update();
    void render();
    
    bool hasSelectedWorkshop() const { return m_hasSelected; }
    bool shouldGoBack() const { return m_shouldGoBack; }

private:
    PlanePilotApp* m_app;
    bool m_hasSelected;
    bool m_shouldGoBack;
};

#endif // WORKSHOP_SELECTOR_H